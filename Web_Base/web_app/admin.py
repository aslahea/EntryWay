from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_per_page = 10

    list_display = (
        'id', 'username', 'full_name', 'email', 'phone', 'gender', 'date_of_birth', 'is_active', 'is_deleted', 'date_joined')

    list_filter = ('is_active', 'is_staff', 'gender',
                   'is_deleted', 'date_joined')

    search_fields = ('username', 'email', 'phone', 'full_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (
            None,
            {
                'fields': ('username', 'password')
            }
        ),
        (
            (
                'Personal Info',
                {
                    'fields': ('full_name', 'email', 'phone', 'gender', 'date_of_birth')
                }
            ),
        ),
        (
            'permissions',
            {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }
        ),
        (
            'Important Dates',
            {
                'fields': ('last_login', 'date_joined')
            }
        ),
        (
            'Soft Delete',
            {
                'fields': ('is_deleted')
            }
        )
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username', 'email', 'phone', 'gender', 'full_name', 'date_of_birth', 'password1', 'password2',
                    'is_active', 'is_active', 'is_staff', 'is_deleted'
                )
            }
        ),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_deleted=False)

    actions = ['soft_delete_selected']

    def soft_delete_selected(self, request, queryset):
        queryset.update(is_deleted=True)
        self.message_user(request, "Selected users have been soft-deleted.")
    soft_delete_selected.short_description = "Soft delete selected users"
