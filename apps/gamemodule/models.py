from django.db import models

class HighScores(models.Model):
 name = models.CharField(max_length = 50)
 score = models.IntegerField(default = 0)
