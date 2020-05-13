from django.urls import path
from .views import ExamListView, ExamDetailView, QuestionListView

urlpatterns = [
    path('', ExamListView.as_view(), name='exam-home' ),
    path('exam/<int:pk>/', ExamDetailView.as_view(), name='exam_detail' ),
    path('exam/<int:exam_id>/take', QuestionListView, name='exam_take' ),
]