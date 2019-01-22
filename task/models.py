from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name