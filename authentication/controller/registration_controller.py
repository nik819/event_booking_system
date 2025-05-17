import logging
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from authentication.services.registration_service import RegistrationService, LoginService


service=RegistrationService

class Registration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            logging.info(data)
            respone=service.registration_service(data)
            if 'error' in respone:
                return Response({'error':respone['error']},status=status.HTTP_400_BAD_REQUEST)
            return Response(respone, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : str(e)},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginController(APIView):
     permission_classes=[AllowAny]
     def post(self,request):
        try:
            emailOrUsername = request.data.get('emailOrUsername')
            password = request.data.get('password')
            # Check if email and password are provided
            if not emailOrUsername or not password:
                return Response({'message': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
            response=LoginService.login_service(emailOrUsername,password)
            if 'error' in response:
                status_code = response.get('status', 400)
                return Response({'message': response['error']}, status=status_code)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)