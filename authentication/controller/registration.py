from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class Registration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : str(e)},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)
