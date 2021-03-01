from django.db import models

# Create your models here.
class Memo(models.Model) :
    title = models.CharField(max_length=500)
    cont = models.TextField()
    input_date = models.DateField(null=True)

    def __str__(self):
        return self.title