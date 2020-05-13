from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Exam, Question, Category
from mcq.models import MCQ, Choice
# Create your views here.


class ExamListView(ListView):
    model = Exam
    template_name = 'exam/home.html'
    context_object_name = 'exams'



class ExamDetailView(DetailView):
    model = Exam
    # template_name = 'exam/exam_detail.html'
    context_object_name = 'exam'


def QuestionListView(request, exam_id):
    context ={
        'questions': get_questions(exam_id)
    }
    if request.POST:
        for item in request.POST:
            print(item)
        messages.success(request, 'Your exam has been submitted successfully!.')
        return redirect('exam_detail', exam_id)
    return render(request, 'exam/take_exam.html', context)


def get_questions(exam_id):
    cats = Category.objects.filter(exam_name = exam_id)
    qns = []
    for cat in cats:
        qns_in_cat = MCQ.objects.filter(category=cat.pk)
        for qn in qns_in_cat:
            qns.append({'qn': qn, 'choices': qn.get_choices_list})
    return qns