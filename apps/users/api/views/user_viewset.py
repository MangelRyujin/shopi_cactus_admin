
from apps.users.api.serializers.user_serializer import UserSerializer, Password_SetSerializer, UpdateUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action


class UserViewSet(viewsets.GenericViewSet):
    serializer_class= UserSerializer
    
    
    def get_queryset(self,pk = None):
        if pk is not None:
            return self.serializer_class().Meta.model.objects.filter(id=pk).first()
        return self.serializer_class().Meta.model.objects.all()

    def list(self,request, *args, **kargs):
        
        user = self.get_queryset()
        if user is not None:
            user_serializer = self.serializer_class(user,many=True)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existen los usuarios!'},status = status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,pk=None):
        
        user = self.get_queryset(pk)
        if user is not None:
            user_serializer = self.serializer_class(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe el usuario!'},status = status.HTTP_404_NOT_FOUND)

    
    def update(self,request,pk=None):
            user = self.get_queryset(pk)
            if user:
                user_serializers = UpdateUserSerializer(user ,data = request.data)
                if user_serializers.is_valid():
                    user_serializers.save()
                    return Response({'message':'Usuario editado correctamente!'}, status = status.HTTP_200_OK)
                else:
                    return Response({'message':'Error al editar los datos!','errors':user_serializers.errors},status = status.HTTP_400_BAD_REQUEST) 
            return Response({'message':'No existe el usuario que desea editar!'},status = status.HTTP_404_NOT_FOUND)
        
    
    
    def destroy(self, request,pk=None):
        
        user = self.get_queryset(pk)
        if user:
            user.delete()
            return Response({'message':'El usuario ha sido eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe el usuario que desa eliminar!'},status = status.HTTP_404_NOT_FOUND)
        
        
    @action(detail = True, methods = ['post'])
    def set_password(self,request,pk=None):
        user = self.get_queryset(pk)
        password_serializer = Password_SetSerializer(data = request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'message':'Contraseña actualizada correctamente'},status = status.HTTP_200_OK)

        return Response({'message':'Error al enviar datos','error':password_serializer.errors},status = status.HTTP_400_BAD_REQUEST)
    