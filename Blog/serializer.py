from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'home', 'about', 'blog', 'contact')

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Blog.objects.filter(id=instance.id).update(**validated_data)
        return Blog.objects.get(id=instance.id)

    def delete(self, instance, validated_data):
        Blog.objects.filter(id=instance.id).update(**validated_data)
