from django.contrib import admin
from app1.models import *

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['cname','duration','fee']

