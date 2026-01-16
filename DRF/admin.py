from django.contrib import admin

from DRF.models import Employee, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)