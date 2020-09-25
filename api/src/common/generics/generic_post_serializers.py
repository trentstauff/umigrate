from users.serializers import BasicUserSerializer
from rest_framework import serializers
from .generic_serializers import GenericSerializer


# Serializes a generic resource model
class GenericPostSerializer(GenericSerializer):
    creator = BasicUserSerializer(read_only=True)
    liked_users = BasicUserSerializer(read_only=True, many=True)
    tagged_users = BasicUserSerializer(read_only=True, many=True)
    is_liked = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_is_liked(self, instance):
        return instance.liked_users.filter(id=self.context['request'].user.id).exists()

    def get_likes(self, instance):
        return instance.liked_users.count()

    def get_comments(self, instance):
        return instance.comment_set.count()

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(creator_id=self.context['request'].user.id, **validated_data)
        return instance


# Serializes a generic comment model
class GenericCommentSerializer(GenericSerializer):
    creator = BasicUserSerializer(read_only=True)
    liked_users = BasicUserSerializer(read_only=True, many=True)
    tagged_users = BasicUserSerializer(read_only=True, many=True)
    is_liked = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    def get_is_liked(self, instance):
        return instance.liked_users.filter(id=self.context['request'].user.id).exists()

    def get_likes(self, instance):
        return instance.liked_users.count()

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(creator_id=self.context['request'].user.id, **validated_data)
        return instance
