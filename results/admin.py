from django.contrib import admin

from .models import ExamTaker, UserAnswers

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = UserAnswers

class ExamTakerAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(ExamTaker, ExamTakerAdmin)