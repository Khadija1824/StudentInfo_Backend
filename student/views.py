from django.shortcuts import render
from student.models import Student

# import pdb;pdb.set_trace()
# Create your views here.
def student_list(request):
   
    students=[]
    student_name=request.GET.get('studentname')
    father_name=request.GET.get('fathername')
    # import pdb;pdb.set_trace()
    if student_name  and father_name:
        students=Student.objects.filter(name=student_name,fathername=father_name)
    elif father_name:  
           students=Student.objects.filter(fathername=father_name)
    elif  student_name:
        students=Student.objects.filter(name=student_name)
                  
    else:
        students=Student.objects.all()
   
    print("students", students)
    student_dict={'student_list':students}
    return render(request, 'student_table_page.html',student_dict)
