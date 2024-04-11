from django.db import models
 
class Artist(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
       
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Track(models.Model):
    name = models.CharField(max_length=150)
    composer = models.CharField(max_length=100)
    milliseconds = models.BigIntegerField(default=0)
    bytes = models.DecimalField(default=0.)
    unitPrice = models.DecimalField(default=0.)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
