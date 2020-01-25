from rest_framework import serializers as sz
from django.contrib.auth.models import User

class UserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','is_superuser','first_name', 'last_name')

class UserSerializerWithToken(sz.ModelSerializer):    
    password = sz.CharField(write_only=True)
    token = sz.SerializerMethodField()    
    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER        
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)        
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance    
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name',
        'last_name')