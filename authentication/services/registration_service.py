from authentication.repository.registration_repository import RegistrationRepository

repo=RegistrationRepository

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