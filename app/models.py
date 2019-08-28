from django.db import models

# Create your models here.


class EmailStore(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    is_edited = models.BooleanField(default=False)