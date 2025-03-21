from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from .models import Post

class CustomUserAdmin(UserAdmin):

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'profile'),
        }),
    )

    # Fields to display in the admin user edit form
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Profile', {'fields': ('profile',)}),  # Add the profile field here
    )

    # Fields to display in the user list view
    list_display = ('username', 'email', 'is_staff', 'profile')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Post)

