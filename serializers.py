from rest_framework import serializers
from .models import CustomUser, File, DownloadLink

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_ops_user', 'is_client_user', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            is_ops_user=validated_data['is_ops_user'],
            is_client_user=validated_data['is_client_user']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'user', 'file', 'uploaded_at']

class DownloadLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadLink
        fields = ['file', 'link', 'created_at', 'is_active']
