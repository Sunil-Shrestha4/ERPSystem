from django.contrib import admin

# Register your models here.
from .models import User
from .models import Department
from .models import Attendance
from .models import Salary,RegisterUser,Leave


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(RegisterUser)
admin.site.register(Leave)
