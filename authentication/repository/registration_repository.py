from authentication.serilizers import RegistrationSerializers
from authentication.models import User
from django.db.models import Q


class RegistrationRepository:
    @staticmethod
    def registration_repository(data):
        try:
            serializer = RegistrationSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return {'message': 'Registration Successful'}
            else:
                return {'error': serializer.errors}
        except Exception as e:
            return {'error': str(e)}
        
    def login_repository(emailorusername,password):
        try:
            user=User.objects.filter(Q(email=emailorusername) | Q(username=emailorusername)).first()
            if user and user.check_password(password):
                return {'message':f'login successfully {user.first_name}'} 
            else:
                return {'error':'Invalid Credancials'}
        except Exception as e:
            return {'error':str(e)}
