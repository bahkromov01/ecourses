from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    education = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Blog, related_name='author', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    reader_name = models.ForeignKey(Author, related_name='reader_name', on_delete=models.CASCADE, null=True, blank=True)
    reader_email = models.ForeignKey(Author, related_name='reader_email', on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE, null=True, blank=True)


