from django.contrib import admin
from .models import Teacher, Student

@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'T_name', 'Designation', 'Username', 'Pass_word', 'Moblie_number', 'Email', 'DOB', 'Date_of_Joining']
# Register your models here