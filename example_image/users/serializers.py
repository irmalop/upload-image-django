from rest_framework.serializers import ModelSerializer
from .models import User
import cloudinary

class  UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions',)
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.name=validated_data.get('name', None)
        image = validated_data.get('image', None)
        if not image is None:
            upload_data = cloudinary.uploader.upload(image, folder = f'media/photos_users/{validated_data.get("email")}')
            user.image = upload_data["secure_url"]
        user.save()
        return user
    
class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'status_delete', 'is_active',
                   'is_superuser', 'password', 'user_permissions', 'groups',)
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.pop('image')
        response.setdefault('image', instance.image.public_id)
        return response