from django.db import models

from courses.models import Course, Category


# Create your models here.

class Teachers(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'Junior'
        MIDDLE = 'Middle'
        SENIOR = 'Senior'
    full_name = models.CharField(max_length=100)
    courses = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='teachers', null=True, blank=True)
    specialty = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(choices=LevelChoices.choices, default=LevelChoices.SENIOR, max_length=100)


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