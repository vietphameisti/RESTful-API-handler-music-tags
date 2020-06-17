from django.db import models

# Create your models here.
class Tag(models.Model):
    #id_tag  =models.AutoField(primary_key=True)
    tag_name=models.CharField(max_length=50)
    class Meta:
        db_table='Tag'

class Track(models.Model):
    #id_track  =models.AutoField(primary_key=True)
    track_name=models.CharField(max_length=120)
    track_tag =models.ManyToManyField(Tag)
    class Meta:
        db_table='Track'

class Album(models.Model):
    #id_album  =models.AutoField(primary_key=True)
    album_name=models.CharField(max_length=120)
    album_tag =models.ManyToManyField(Tag)
    class Meta:
        db_table='Album'

class Artist(models.Model):
    #id_album   =models.AutoField(primary_key=True)
    artist_name=models.CharField(max_length=120)
    artist_tag =models.ManyToManyField(Tag)
    class Meta:
        db_table='Artist'