from django.contrib import admin

# Register your models here.
from .models import User,Department,Attendance,Salary,RegisterUser,Leave,Attendance

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(RegisterUser)
admin.site.register(Leave)
