from django.db import models

from courses.models import Course


# Create your models here.

class Teachers(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    courses = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE, null=True, blank=True)
    specialty = models.TextField(blank=True)


class Comment(models.Model):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='comments')