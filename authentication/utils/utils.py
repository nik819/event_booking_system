import random
import threading

from authentication.config.config import OTP_CONFIG
from django.core.mail import send_mail

def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(OTP_CONFIG["otp_length"])])

def send_otp_email(email, otp):
    subject = "Your OTP for Two Stap Verification"
    message = f"Use this OTP to complete your login: {otp}. It is valid for {OTP_CONFIG['otp_expiry']} seconds."
    from_email = "joshinikhil404@gmail.com"
    send_mail(subject, message, from_email, [email])

def send_otp_email_async(email, otp):
    print("********", email, "*****", otp)
    threading.Thread(target=send_otp_email, args=(email, otp)).start()
