from django.forms import ModelForm
from .models import ExamTaker, UserAnswers


class ExamTakerForm(ModelForm):
    class Meta:
        model = ExamTaker
        fields = '__all__'

class MCQForm(ModelForm):
    class Meta:
        model = UserAnswers
        fields = '__all__'