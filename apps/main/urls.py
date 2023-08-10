from django.urls import path

from .views import post_list, create_post, delete_post, update_post

urlpatterns = [
    # path('posts/', post_list),
    path('', post_list),
    path('create/', create_post),
    path('delete/<int:post_id>/',delete_post),
    path('update/<int:post_id>/',update_post),
]