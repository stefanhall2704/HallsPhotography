from django.db import models

# Create your models here.
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    watermarked_photo = models.UUIDField()
    non_watermarked_photo = models.UUIDField()