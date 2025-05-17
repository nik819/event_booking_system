from authentication.repository.registration_repository import RegistrationRepository, LoginRepository
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