from django.db import models

# Create your models here.
class Hymn(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.number} {self.title}'
    
class Verse(models.Model):
    hymn = models.ForeignKey(Hymn, on_delete=models.CASCADE)
    verse_number = models.IntegerField(name='verse_number')
    verse = models.TextField()
    
    class Meta:
        indexes = [
            models.Index(fields=['hymn', 'verse_number'], name='hymn_verse_number_idx'),
        ]

    def __str__(self):
        return f'{self.hymn.number} {self.hymn.title} {self.verse_number} {self.verse}'
