from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="art_posts"
    )
    banner = models.ImageField(default='default.jpg', blank=True)

    #featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

#add permission start


#class MyModel(models.Model):
    #name = models.CharField(max_length=100)

    #class Meta:
        #permissions = [
            #("can_view_mymodel", "Can view MyModel"),
        #]

#end

#Geza
class CollaborateRequest(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    banner = models.ImageField(default='default.jpg', blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    #def __str__(self):
       # return self.title

