from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    genre = models.CharField(max_length=200, default='')
    logo = models.FileField(default='music/static/music/images/fav star.jpg')
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title+" by "+self.artist

class Song(models.Model):
    title = models.CharField(max_length=200)
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    filetype=models.CharField(max_length=6)
    file=models.FileField(default='music/static/music/images/fav star.jpg')
    likes=models.IntegerField(default=0)
    def __str__(self):
        return self.title+" by "+self.album.artist