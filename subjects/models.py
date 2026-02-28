from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Topic(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='topics')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

