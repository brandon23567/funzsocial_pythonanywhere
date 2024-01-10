from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_all_posts/", views.get_all_posts, name="get_all_posts"),
    path("get_single_post/<str:slug>/", views.get_single_post, name="get_single_post"),
    path("upload_post/", views.upload_post, name="upload_post"),
]
