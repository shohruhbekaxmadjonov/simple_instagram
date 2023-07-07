from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, Post, Like, Comment, Follow
from .pagination import FollowerPagination
from .permissions import CanUpdateProfile, IsPublisherOrReadOnly
from .serializers import UserSerializer, PostSerializer, LikeSerializer, CommentSerializer, FollowingSerializer, \
    UserDetailSerializer, FollowersSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = FollowerPagination


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [CanUpdateProfile, IsAuthenticated]


class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPublisherOrReadOnly]


class CreateLike(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class PostLikes(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Like.objects.filter(post_id=pk)


class DeleteLike(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [CanUpdateProfile]


class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsPublisherOrReadOnly]


class CreateFollowing(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]


class FollowingRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [IsPublisherOrReadOnly]


class FollowingList(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [IsPublisherOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Follow.objects.filter(follower_id=pk)


class FollowersList(generics.ListAPIView):
    serializer_class = FollowersSerializer
    permission_classes = [IsPublisherOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Follow.objects.filter(following_id=pk)
