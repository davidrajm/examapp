from django.contrib import admin
from .models import Exam, Category, Question

from mcq.models import MCQ, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice

class MCQAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]




admin.site.register(Exam)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(MCQ, MCQAdmin)