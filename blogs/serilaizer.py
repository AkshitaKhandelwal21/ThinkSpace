from rest_framework import serializers

from blogs.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']
        read_only_fields = ['slug', 'author']
