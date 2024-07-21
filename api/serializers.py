from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields=['usename','email']

class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        author= UserSerializer()
        fields=["id", "author", "title", "body", "created", "updated"]
        depth= 1