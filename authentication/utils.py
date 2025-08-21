import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

from core.config import conf

EMAIL_HOST = conf.email.EMAIL_HOST
EMAIL_PORT = conf.email.EMAIL_PORT
EMAIL_USER = conf.email.EMAIL_USER
EMAIL_PASSWORD = conf.email.EMAIL_PASSWORD

env = Environment(loader=FileSystemLoader('templates'))


def send_email(receiver: str, subject: str, body: str):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = EMAIL_USER
    message["To"] = receiver

    part2 = MIMEText(body, "html")
    message.attach(part2)

    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, receiver, message.as_string())


def send_verification_code(receiver: str, code: str):
    subject = "Your Verification Code"
    template = env.get_template("verification_email.html")
    body = template.render({"code": code})
    send_email(receiver, subject, body)


def generate_code(self) -> str:
    return str(randint(100000, 999999))