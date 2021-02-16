from rest_framework import serializers
from .models import CodePost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodePost
        fields = ['id', 'title', 'body', 'author', 'updated_at']
