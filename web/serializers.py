from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        # fields = ('title', 'content', 'created_dt', 'updated_dt')
        fields = '__all__'