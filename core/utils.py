import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from core.config import conf

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465

EMAIL_USER = conf.redis.EMAIL_USER
EMAIL_PASSWORD = conf.redis.EMAIL_PASSWORD

RECEIVER = 'ochildiyevajasmina@gmail.com'


from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))



def send_email(receiver, subject, body):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = EMAIL_USER
    message["To"] = receiver
    part2 = MIMEText(body, "html")
    message.attach(part2)

    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, RECEIVER, message.as_string())


def verification_code(receiver):
    subject = "Verification Code"

    template = env.get_template('verification_email.html')

    context = {
        'code': '123456'
    }

    body = template.render(context)

    send_email(receiver, subject, body)

