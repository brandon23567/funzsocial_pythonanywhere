from django.db import models

class BlogPost(models.Model):
    username = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    short_description = models.TextField()
    header_image = models.ImageField(upload_to="header_images/", blank=True, null=True)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
