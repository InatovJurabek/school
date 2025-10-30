from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.assignments.models import StudentAnswer
from .serializers import StudentAnswerSerializer 



class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

    def perform_create(self, serializer):
        student = self.request.user
        answer = serializer.save(student=student)
        if answer.selected_option:
            answer.is_correct = answer.selected_option.is_correct
            answer.points_earned = 1 if answer.is_correct else 0
            answer.feedback = "Correct!" if answer.is_correct else "Incorrect!"
        elif answer.text_answer:
            answer.feedback = "Answer received. AI evaluation pending."
        elif answer.code_answer or answer.file_answer:
            answer.feedback = "Your answer will be reviewed by teacher."
        answer.save()
        return answer


@api_view(['GET'])
def answer_list(request):
    answers = StudentAnswer.objects.all()
    serializer = StudentAnswerSerializer(answers, many=True)
    return Response(serializer.data)  


def answer_detail(request, pk):
    try:
        answer = StudentAnswer.objects.get(id=pk)
    except StudentAnswer.DoesNotExist:
        return Response({'error': 'Answer not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentAnswerSerializer(answer)
    return Response(serializer.data)


@api_view(['POST'])
def answer_create(request):
    serializer = StudentAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def answer_update(request, pk):
    try:
        answer = StudentAnswer.objects.get(id=pk)
    except StudentAnswer.DoesNotExist:
        return Response({'error': 'Answer not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentAnswerSerializer(answer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def answer_delete(request, pk):
    try:
        answer = StudentAnswer.objects.get(id=pk)
    except StudentAnswer.DoesNotExist:
        return Response({'error': 'Answer not found'}, status=status.HTTP_404_NOT_FOUND)
    answer.delete()
    return Response({'message': 'Answer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


