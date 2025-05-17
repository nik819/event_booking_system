import os

OTP_CONFIG = {
    "otp_length": os.getenv('DOCUMENTMANAGEMENT_EMAIL_OTP_LENGTH',4),
    "otp_expiry": os.getenv('DOCUMENTMANAGEMENT_EMAIL_OTP_EXPIRY',180),
    "verification_attempts_allowed": os.getenv('DOCUMENTMANAGEMENT_EMAIL_OTP_VERIFICATION_ATTEMPTS',5),
}
