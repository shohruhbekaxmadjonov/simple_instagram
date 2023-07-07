from rest_framework import serializers
from .models import User, Post, Like, Comment, Follow


class UserDetailSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile_picture', 'bio', 'followers_count',
                  'followings_count', 'posts_count']
        extra_kwargs = {'password': {'write_only': True}}

    def get_followers_count(self, instance):
        return instance.followers.count()

    def get_followings_count(self, instance):
        return instance.following.count()

    def get_posts_count(self, instance):
        return instance.post_set.count()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile_picture']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['user', 'image', 'caption', 'comments_count', 'likes_count']

    def get_likes_count(self, instance):
        return instance.likes.count()

    def get_comments_count(self, instance):
        return instance.comments.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FollowingSerializer(serializers.ModelSerializer):
    following = UserSerializer()

    class Meta:
        model = Follow
        fields = '__all__'


class FollowersSerializer(serializers.ModelSerializer):
    follower = UserSerializer()

    class Meta:
        model = Follow
        fields = "__all__"
