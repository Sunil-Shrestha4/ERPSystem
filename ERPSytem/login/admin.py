from django.contrib import admin

# Register your models here.
from .models import User
from .models import Department
from .models import Attendance
from .models import Salary,Leave,UserDetails,MyLeave,Holiday


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Salary)

admin.site.register(Holiday)
# admin.site.register(Leave)
admin.site.register(UserDetails)
admin.site.register(MyLeave)

