from django.conf import settings
from django.core.mail import send_mail



def send_email_token(email, verify_url):
    try:
        subject = 'Your account needs to be verified'
        message = f'Hi,\n\nPlease click the following link to verify your account:\n\n{verify_url}\n\nIf you did not request this verification, please ignore this email.\n\nThank you.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        return False
