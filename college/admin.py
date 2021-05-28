from django.contrib import admin
from college.models import Notice, Student
from django.contrib.admin.options import ModelAdmin

# Register your models here.
#django uses display, search and filter as keywords and perform operations accordingly.
class NoticeAdmin(ModelAdmin):
    list_display = ["subject" , "cr_date"]
    search_fields = ["subject" , "msg"]
    list_filter = ["cr_date"]

# Register table in admin.
admin.site.register(Notice, NoticeAdmin)

class StudentAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name" , "address"]

# Register table in admin.
admin.site.register(Student, StudentAdmin)
