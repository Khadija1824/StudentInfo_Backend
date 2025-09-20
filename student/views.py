from django.shortcuts import render
from student.models import Student

# Create your views here.
def student_list(request):
   students=Student.objects.all()
   print("students", students)
   student_dict={'student_list':students}
   return render(request, 'student_table_page.html',student_dict)
