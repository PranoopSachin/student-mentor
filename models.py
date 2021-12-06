from django.db import models
from users.models import User


class Question(models.Model):
    id = models.PrimaryKey()
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer_id = models.ForeignKey(on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    
 class Answer(models.Model):
    id = models.PrimaryKey()
    answer = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice) 

    def __str__(self):
        return self.question

  
