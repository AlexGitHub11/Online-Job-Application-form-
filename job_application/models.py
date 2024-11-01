from django.db import models

class Form(models.Model):
    # define db
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # Magic method to display instance of class as string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
