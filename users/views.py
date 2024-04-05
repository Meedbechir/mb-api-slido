from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate
from users.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


#Generate Token Manually
def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        }
#Ckeck mails
class CheckEmailExistsView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if email:
            user_model = get_user_model()
            if user_model.objects.filter(email=email).exists():
                return Response({'exists': True}, status=status.HTTP_200_OK)
            else:
                return Response({'exists': False}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email not provided'}, status=status.HTTP_400_BAD_REQUEST)

#Registration
class UserRegistrationView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, format=None):
                serializer = UserRegistrationSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                        user = serializer.save()
                        token = get_tokens_for_user(user)
                        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login
class UserLoginView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, format=None):
                serializer = UserLoginSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                        email = serializer.data.get('email')
                        password = serializer.data.get('password')
                        user = authenticate(email=email, password=password)
                        if user is not None:
                                token = get_tokens_for_user(user)
                                return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
                        else:
                                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

#Reset password
class SendPasswordResetEmailView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, format=None):
                serializer = SendPasswordResetEmailSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                        return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, uid, token, format=None):
                serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
                if serializer.is_valid(raise_exception=True):
                        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)