from rest_framework import serializers
from ..models import Bibliotecario

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_reenter = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = Bibliotecario
        fields = ('usuario', 'password', 'password_reenter', 'email', 'nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_reenter']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_reenter')
        user = Bibliotecario.objects.create_user(
            usuario=validated_data['usuario'],
            email=validated_data['email'],
            password=validated_data['password'],
            nombres=validated_data['nombres'],
            apellido_paterno=validated_data['apellido_paterno'],
            apellido_materno=validated_data['apellido_materno'],
            direccion=validated_data['direccion'],
            telefono=validated_data['telefono']
        )
        return user

class BibliotecarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecario
        fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'email', 'is_active']