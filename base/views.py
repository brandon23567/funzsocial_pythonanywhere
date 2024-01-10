from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BlogPost
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

@api_view(["GET"])
def index(request):
    return Response({"message": "This is working just testing static files with pythonanywhere"})


@api_view(["GET"])
def get_all_posts(request):
    all_posts = BlogPost.objects.all().order_by("-date_posted")

    posts = []

    for post in all_posts:
        post_data = {
            "username": post.username,
            "title": post.title,
            "slug": post.slug,
            "short_description": post.short_description,
            "header_image": post.header_image.url,
            "body": post.body
        }

        posts.append(post_data)
    return Response(posts)

@api_view(["GET"])
def get_single_post(request, slug):
    current_post = get_object_or_404(BlogPost, slug=slug)
    if current_post is not None:
        post_data = {
            "username": current_post.username,
            "title": current_post.title,
            "slug": current_post.slug,
            "short_description": current_post.short_description,
            "header_image": current_post.header_image.url,
            "body": current_post.body
        }

        return Response(post_data)
    else:
        return Response({"message": "No such post here fix the url and slug thingy and how it works g"})

@api_view(["POST"])
def upload_post(request):
    blog_title = request.data.get("title")
    user_uploading = request.data.get("username")
    short_description = request.data.get("description")
    blog_content = request.data.get("postBody")
    header_image = request.FILES.get("headerImage")
    post_slug = blog_title

    new_post = BlogPost.objects.create(username=user_uploading, title=blog_title, slug=post_slug, short_description=short_description, header_image=header_image, body=blog_content)
    new_post.save()

    return Response({"message": "New post has been created successfully"})