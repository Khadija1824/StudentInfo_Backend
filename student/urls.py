# from student.views import student_list
from django.urls import path,include
from student import views

urlpatterns = [
    path('', views.student_list, name="student_list"),
]