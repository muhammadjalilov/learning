from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.courses.validators import validate_start_date_less_than_end_date
from apps.shared.models import SlugStampedModel


class Course(SlugStampedModel):
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    max_students = models.PositiveSmallIntegerField()
    intro_video_link = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    instructor = models.ForeignKey('instructors.Instructor', on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="courses")

    def clean(self):
        super().clean()
        validate_start_date_less_than_end_date(self.start_date, self.end_date)

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


class Topic(SlugStampedModel):
    duration = models.TimeField()
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name
