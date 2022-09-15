from rest_framework import generics, permissions
from rest_framework.response import Response
from applications.user.api.serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

""" #Esta vista no permite el metodo GET. Por ello si queremos mostrar, nos dice los siguiente: {"detail":"Método \"GET\" no permitido."}
class Login(ObtainAuthToken):
    def post(self, request,*args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = { 'request':request })
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                created,token = Token.objects.get_or_create(user = user) #Este ORM de Django retorna dos cosas, la instancia(el token) y un booleano si sea creado o no(created).
                user_serializer =  UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesion exitoso.'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesion.'}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Nombre de usuario y/o constraseña inccorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Hola desde response'}, status = status.HTTP_200_OK) """

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })
        else:
            return Response({'message':'Datos incorrectos, por favor reintentelo.'})
    

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)