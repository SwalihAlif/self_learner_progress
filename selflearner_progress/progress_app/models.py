from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
