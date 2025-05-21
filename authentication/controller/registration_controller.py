import logging
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.services.registration_service import RegistrationService, LoginService, ForgotPasswordService,OtpVerificationService,OtpResendService,RoleService


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

class ForgotPasswordController(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        try:
            email = request.data.get('emailOrUsername')
            if not email:
                return Response({'message': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
            response=ForgotPasswordService.forgot_password_service(email)
            if 'error' in response:
                return Response({'message': response['error']}, status=status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# otpverification controller
class OtpVerification(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        try:
            logging.info('otpverification api callig...')
            user_id = request.data.get('userId')
            otp = request.data.get('otp')
            logging.info(f'request data  :{request.data}')
            if not user_id or not otp:
                return Response({'message': 'Email and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)
            # Call the service to verify OTP
            response ,status_code= OtpVerificationService.otp_verification_service(user_id, otp)
            if status_code == 429:
                return Response({'message': 'Maximum OTP attempts exceeded. Please request a new OTP.'},status=status.HTTP_429_TOO_MANY_REQUESTS)
            elif status_code == 410:
                return Response({'message': 'OTP has expired.'},status=status.HTTP_410_GONE)
            elif status_code == 404:
                return Response({"message": "User not found"},status=status.HTTP_404_NOT_FOUND)
            elif status_code == 400:
                return Response({"message":"Invalid OTP"},status=status.HTTP_400_BAD_REQUEST)
            else:  
                return Response(response, status_code)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AccessTokenGenerate(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        logging.info("accress token api calling....")
        refresh_token=request.data.get('refresh')
        if not refresh_token:
                return Response({'message': 'Invalid RequestBody'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)
            return Response({"access": new_access_token})
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
        
class ResendOtpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            logging.info('Resend OTP API called...')
            user_id = request.data.get('userId')
            logging.info(f'request data  :{request.data}')
            if not user_id:
                return Response({'message': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Call the service to resend OTP
            response= OtpResendService.resend_otp_service(user_id)
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class RoleInformation(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        logging.info('Role information api')
        try:
            # Call the service to resend OTP
            page= int(request.query_params.get('page',1))
            size= int(request.query_params.get('size',5))
            response,count=RoleService.role_service(page,size)
            return Response({'count':count,'resultset':response},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
