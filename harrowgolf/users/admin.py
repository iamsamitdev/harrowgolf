from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, Student

admin.site.site_header = "Harrow Golf Academy Admin"
admin.site.site_title = "Harrow Golf Academy"
admin.site.index_title = "Welcome to Harrow Golf Academy"

admin.site.register(User, UserAdmin, list_display=['username', 'email', 'first_name', 'last_name', 'is_student', 'is_teacher'])
admin.site.register(Student, list_display=['user', 'first_name', 'last_name','created_at'] )
admin.site.register(Teacher, list_display=['user', 'academy_name', 'first_name', 'last_name','created_at'])

