
from courses.models import Category
from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/blog')
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        return reverse('blogs', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class Blog_list(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(upload_to='images/')
    blog_id = models.ForeignKey(Blog_list, on_delete=models.CASCADE)


class BlogComment(models.Model):
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog_list, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description

        return titlestring



