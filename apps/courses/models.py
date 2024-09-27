from django.db import models

from apps.shared.models import SlugStampedModel


class Course(SlugStampedModel):
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    max_students = models.IntegerField()
    intro_video_link = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    rating = models.IntegerField()
    instructor = models.ForeignKey('apps.Instructor', on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey()

    def __str__(self):
        return self.name


class Category(SlugStampedModel):
    description = models.TextField()

    def __str__(self):
        return self.name


class Chapter(SlugStampedModel):
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.name


class Theme(SlugStampedModel):
    duration = models.TimeField()
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='themes')

    def __str__(self):
        return self.name

