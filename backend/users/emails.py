from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User

def send_otp(email):
    subject = 'Account Verification Email'
    otp = random.randint(100000,999999)
    email_from = settings.EMAIL_HOST_USER
    message = f'Your otp to verify the account is {otp}'
    send_mail(subject, message,email_from, [email])
    user_obj= User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()