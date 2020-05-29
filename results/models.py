from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User
from exam.models import Exam, Question
from mcq.models import Choice


class ExamTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    started_at = models.DateTimeField(default = timezone.now)
    completed_at = models.DateTimeField(default = timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.exam.sub_code}: {self.user.first_name}'

    
class UserAnswers(models.Model):
    user = models.ForeignKey(ExamTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete= models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE, null=True)