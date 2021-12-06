from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import Questions
from .serializers import QuestionsSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class =QuestionSerializer
    queryset = Questions.objects.all()

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.create(request)
            if question:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class AnswerView(ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        queryset = GradedAssignment.objects.all()
        question_id = self.request.query_params.get('question_id', None)
        if username is not None:
            queryset = queryset.filter(question=question_id)
        return queryset



