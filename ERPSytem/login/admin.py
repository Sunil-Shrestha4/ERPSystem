from django.contrib import admin

# Register your models here.
from .models import (Attendance, Department, Leave, LeaveType, Salary, User,
                     UserDetails)

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(Leave)
admin.site.register(LeaveType)
admin.site.register(UserDetails)
