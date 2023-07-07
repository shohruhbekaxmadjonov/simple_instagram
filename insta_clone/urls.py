from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from insta_clone.views import UserList, CreateUser, UserRetrieveUpdateDelete, PostRetrieveUpdateDelete, DeleteLike, \
    CreateFollowing, CommentRetrieveUpdateDelete, CreateComment, CreateLike, CreatePost, \
    FollowersList, FollowingList, PostLikes

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserList.as_view(), name='users'),
    path('create-user/', CreateUser.as_view(), name='create-user'),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-detail'),
    path('create-post/', CreatePost.as_view(), name='create-user'),
    path('post/<int:pk>/', PostRetrieveUpdateDelete.as_view(), name='post-detail'),
    path('post/<int:pk>/likes', PostLikes.as_view(), name='post-likes'),
    path('create-like/', CreateLike.as_view(), name='create-like'),
    path('like/<int:pk>/', DeleteLike.as_view(), name='like-detail'),
    path('create-comment/', CreateComment.as_view(), name='create-comment'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDelete.as_view(), name='comment-detail'),
    path('create-following/', CreateFollowing.as_view(), name='create-following'),
    path('user/<int:pk>/followers', FollowersList.as_view(), name='followers_list'),
    path('user/<int:pk>/followings', FollowingList.as_view(), name='Followings_list'),
]
