from django.urls import path
from .views import ShowQuestion

urlpatterns = [
    path('exam/<int:exam_id>/take-exam', ShowQuestion, name='take-exam' ),
]