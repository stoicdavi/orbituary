from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField(default='Content not provided')
    author = models.CharField(max_length=100, default='Anonymous')
    submission_date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
