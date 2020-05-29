from django.shortcuts import render
from django.views.generic import FormView
from .forms import ExamTakerForm, MCQForm
from django.forms import formset_factory
from django.forms.models import inlineformset_factory
# Create your views here.


def ShowQuestion(request, exam_id):
    UserAnswerForm = formset_factory(MCQForm, extra=3)
    context ={
        'forms' : UserAnswerForm()
    }
    return render(request, 'results/take-exam.html', context)
