from django.contrib import admin

from users.models import User

# @admin.register(Categories)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email',]

