from django.db import models

# Create your models here.

# class archery_board(models.Model):
#     name = models.CharField(max_length=264)
#     score = models.CharField(max_length=264)


class feedback_model(models.Model):
    name = models.CharField(max_length=264,unique=True)
    feedback = models.CharField(max_length =264)
    def __str__(self):
        return (self.name)
