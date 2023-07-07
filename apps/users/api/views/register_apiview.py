from rest_framework.decorators import api_view

from apps.users.api.serializers.user_serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_client_api_view(request):   
    # create
    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        try:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'message':'Successful registration'}, status= status.HTTP_201_CREATED)
            return Response({'error':user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        except: 
            return Response({'message':'Ya existe el usuario'}, status = status.HTTP_400_BAD_REQUEST)