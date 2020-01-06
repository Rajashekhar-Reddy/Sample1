from django.contrib import admin
from .models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['sname','slname','semail','susername','snumber','sgender','sdob','squalification','sadress','spassword']
    search_fields=['sname','slname','sgender']
    list_filter=['sname','slname','sgender']

admin.site.register(student,studentadmin)
