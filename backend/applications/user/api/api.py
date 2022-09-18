""" from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from applications.user.api.serializers import UserSerializer

from rest_framework.response import Response """


""" class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data)

@api_view(['GET','POST'])
def user_apiview(request):
    if request.method == 'GET': #Si es un get, en este caso mostrara por pantalla los usuarios que estan registrados.
        print(PruebaSerializer)
        users = User.objects.all() #Aqui listamos todos los usuarios que hay en db
        users_serializer = UserSerializer(users,many=True) #Como User es una lista, debemos decirle a django que serialize cada objeto de la lista con many=True.
        return Response(users_serializer.data, status= status.HTTP_200_OK) #Mostramos en pantalla los datos serializados en JSON.

    elif request.method == 'POST': #Si es un post
        user_serializer = UserSerializer(data = request.data) #Deseserializa el JSOn y lo convierte en objeto
        if user_serializer.is_valid(): #Si todos los datos son validos
            user_serializer.save() #Guarda el objeto en db
            return Response(user_serializer.data, status = status.HTTP_200_OK) #Y retorna todos los datos del usuario creado.
        return Response(user_serializer.errors) #Si tan solo un dato no es valido, entonces retorna los errores.

#Funcion para acceder al detalle de un usuario.
@api_view(['GET','PUT','DELETE'])
def userdetailView(request, pk):
    #Consulta:
    user = User.objects.filter(id=pk).first() #Filtramos el usuario por la primary key(pk) y obtenemos un unico user.
    #Validamos si existe:
    if user:

        # retrieve:
        if request.method == 'GET':
            user_serializer = UserSerializer(user) #Serializamos a JSON, aqui no ira "many=True", debido a que solo queremos un usuario.
            return Response(user_serializer.data, status = status.HTTP_200_OK) #Retornamos el json con los datos de ese usuario.
        
        #update:
        elif request.method == 'PUT': #Si queremos actualizar los detalles de un usuario en particular se utiliza PUT.
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        #delete:
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message':'No se encontro ningun usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
 """