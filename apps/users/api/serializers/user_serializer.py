from rest_framework import serializers
from apps.users.models import User


        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username')
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'first_name':instance.first_name,
            'last_name':instance.last_name,
            'username':instance.username,
            'email':instance.email,
           
        }
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


        
class Password_SetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length =128,min_length =8, write_only = True)
    password2 = serializers.CharField(max_length =128,min_length =8, write_only = True)
    
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Las contraseñas son incorrectas'})
        return data
    
    
        
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('username','email','first_name','last_name')
