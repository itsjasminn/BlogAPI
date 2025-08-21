import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from authentication.services import OTPServices
from core.config import conf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

EMAIL_HOST = conf.email.EMAIL_HOST
EMAIL_PORT = conf.email.EMAIL_PORT
EMAIL_USER = conf.email.EMAIL_USER
EMAIL_PASSWORD = conf.email.EMAIL_PASSWORD

if not all([EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD]):
    raise ValueError(
        "Email configuration is incomplete. Please check EMAIL_HOST, EMAIL_PORT, EMAIL_USER, and EMAIL_PASSWORD.")

try:
    env = Environment(loader=FileSystemLoader('templates'))
except Exception as e:
    logger.error(f"Failed to initialize Jinja2 environment: {e}")
    raise


def send_email(receiver: str, subject: str, body: str) -> bool:
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = EMAIL_USER
        message["To"] = receiver

        part = MIMEText(body, "html")
        message.attach(part)

        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, receiver, message.as_string())
        logger.info(f"Email sent successfully to {receiver}")
        return True
    except smtplib.SMTPException as e:
        logger.error(f"Failed to send email to {receiver}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error while sending email to {receiver}: {e}")
        return False


def send_verification_code(receiver: str, code: str) -> bool:
    try:
        subject = "Your Verification Code"
        template = env.get_template("verification_email.html")
        body = template.render(code=code)
        return send_email(receiver, subject, body)
    except TemplateNotFound:
        logger.error("Verification email template not found")
        return False
    except Exception as e:
        logger.error(f"Error rendering verification email template: {e}")
        return False


if __name__ == "__main__":
    otp_service = OTPServices()
    email = "ochildiyevajasmina@gmail.com"

    code = otp_service.generate_code()
    success, ttl = otp_service.set_code(email, str(code))

    if not success:
        logger.warning(f"Please wait {ttl} seconds before requesting another code for {email}")
    else:
        if send_verification_code(email, code):
            logger.info("Verification code sent successfully!")
        else:
            logger.error("Failed to send verification code")
