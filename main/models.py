from django.db import models

# Create your models here.
class Memo(models.Model) :
    title = models.CharField(max_length=500)
    cont = models.TextField()
    input_date = models.DateField(null=True)

    def __str__(self):
        return self.title

def upload_path(instance, filename) :
    return '/'.join(['covers', str(instance.title), filename])

class Book(models.Model) :
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)