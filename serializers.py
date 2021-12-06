from rest_framework import serializers

from users.models import User
from .models import  Question




class QuestionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Question
        fields = ('id', 'question','answer')


class AnswerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model =Answer
        fields = ('id', 'answer')


