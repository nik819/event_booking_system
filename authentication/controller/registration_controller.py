from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from authentication.services.registration_service import RegistrationService
service=RegistrationService

class Registration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
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
            emailorusername=request.data.get('emailorusername')
            password=request.data.get('password')
            response = service.login_service(emailorusername,password)
            if 'error' in response:
                return Response({'error':response['error']},status=status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : str(e)},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)