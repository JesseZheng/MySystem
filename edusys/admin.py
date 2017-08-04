from django.contrib import admin
from .models import Student,Course,Teacher,Report

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Sno','Sname')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('Tno','Tname')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('Cno','Cname','Cnature','teacher','TimeTable','Place','Exist_Stu')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('student','course','teacher','Score')

admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Report,ReportAdmin)
