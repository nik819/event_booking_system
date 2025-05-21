from authentication.repository.registration_repository import RegistrationRepository, LoginRepository, ForgotPasswordRepository,OtpVerificationRepository,RoleRepository
import logging
repo=RegistrationRepository


class LoginService:
    @staticmethod
    def login_service(emailOrUsername,password):
        logging.info("LoginService: Calling repository for user registration...")
        try:
            response = LoginRepository.login_repository(emailOrUsername,password)
            return response 
        except Exception as e:
            logging.error(f"Registration failed: {str(e)}")
            return {"error": str(e),"status": 500}

class RegistrationService:
    @staticmethod
    def registration_service(data):
        try:
            result=repo.registration_repository(data)
            return result
        except Exception as e:
            return{'error':str(e)}

    def login_service(emailorusername,password):
        try:
            result=repo.login_repository(emailorusername,password)
            return result
        except Exception as e:
            return{'error':str(e)}

class ForgotPasswordService:
    @staticmethod
    def forgot_password_service(email):
        try:
            result=ForgotPasswordRepository.forgot_password_repository(email)
            return result
        except Exception as e:
            return{'error':str(e)}
        
class OtpVerificationService:
    @staticmethod
    def otp_verification_service(userId,otp):
        logging.info("OtpVerificationService: Calling repository for user otp verification")
        try:
            result = OtpVerificationRepository.otp_verification_repository(userId,otp)
            if result.get('status')!=200:
                status=result.get("status")
                return result, status 
            return result, status.HTTP_200_OK
        except Exception as e:
            logging.error(f"Registration failed: {str(e)}")
            return {"error":str(e)}

class OtpResendService:
    @staticmethod
    def resend_otp_service(userId):
        logging.info("OtpResendService: Calling repository for resending OTP")
        try:
            result= OtpVerificationRepository.resend_otp(userId)
            return result
        except Exception as e:
            logging.error(f"Resend OTP failed: {str(e)}")
            return {"error": str(e)}
class RoleService:
    @staticmethod
    def role_service(page,size):
        try:
            result,count=RoleRepository.role_repository(page,size)
            return result,count
        except Exception as e:
            logging.error(f"Resend OTP failed: {str(e)}")
            return {"error":str(e)}