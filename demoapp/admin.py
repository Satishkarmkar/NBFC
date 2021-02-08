from django.contrib import admin
from demoapp.models import Student
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=['fname']
admin.site.register(Student,RegisterAdmin)