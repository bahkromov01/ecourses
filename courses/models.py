from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    # teachers = models.ManyToManyField()
    image = models.ImageField(upload_to="course", null=True, blank=True)
    video = models.FileField(upload_to='media/courses', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def hours(self):
        if self.duration >= 60:
            hours = self.duration // 60
            return hours

    @property
    def minutes(self):
        if self.duration >= 60:
            minutes = self.duration % 60
            return minutes

    objects = models.Manager

    def __str__(self):
        return self.title


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
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
