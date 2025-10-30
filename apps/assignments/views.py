from django.shortcuts import render, get_object_or_404
from apps.assignments.models import StudentAnswer

def index(request):
    answers = StudentAnswer.objects.all()
    return render(request, 'assignments/answer_list.html', {'answers': answers})

def detail(request, pk):
    answer = get_object_or_404(StudentAnswer, pk=pk)
    return render(request, 'assignments/answer_detail.html', {'answer': answer})
