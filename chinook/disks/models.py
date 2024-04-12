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
    name = models.CharField(max_length=150, null=True)
    composer = models.CharField(max_length=100, null=True)
    milliseconds = models.BigIntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
