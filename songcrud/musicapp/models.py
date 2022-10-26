from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.Charfield(max_lenght = 100)
    last_name = models.Charfield(max_lenght = 100)
    age = models.Intergerfield(blank = True)

class Song(models.Model):
    Artiste = models.Foreignkey(Artiste, on_delete.models.CASCADE)
    title = models.Charfield(max_lenght = 40)
    date_released = models.Intergerfield(blank = False)
    likes = models.Intergerfield(blank = True)
    artiste_id = models.Intergerfield(blank = False)

class Lyric(models.Model):
    Song = models.Foreignkey(Song, on_delete.models.CASCADE)
    content = models.Charfield(max_lenght = 400)
    song_id = models.Intergerfield(blank = False)