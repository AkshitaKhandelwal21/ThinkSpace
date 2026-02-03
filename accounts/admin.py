from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

# Register your models here.
class UserModelAdmin(UserAdmin):
    model = User
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'role')


admin.site.register(User, UserModelAdmin)