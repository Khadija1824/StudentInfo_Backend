from django.contrib import admin
from student.models import Student

# Register your models here.
@admin.register(Student)
class UserAdmin(admin.ModelAdmin) :
    list_display = ('id', 'name', 'email','country','fathername','mothername')