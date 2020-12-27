from django.contrib import admin

# Register your models here.
from .models import User,RegisterUser,Leave

admin.site.register(User)
admin.site.register(RegisterUser)
admin.site.register(Leave)
