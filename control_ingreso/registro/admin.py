from django.contrib import admin
from .models import Employee, Visitor, Attendance, Area

admin.site.register(Employee)
admin.site.register(Visitor)
admin.site.register(Attendance)
admin.site.register(Area)