from django.contrib import admin
from user.models import Customer
from django.utils.safestring import mark_safe


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'get_image', 'phone',
                    'website', 'country', 'city',
                    )
    list_filter = ('country', 'city')
    fieldsets = (
        (None, {'fields': (
            'name', 'email', 'phone', 'password', 'avatar',
            'country', 'city', 'website'
            )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'email', 'phone', 'avatar',
                'password1', 'password2', 'country', 'city', 'is_staff',
                'is_active',
                )}
         ),
    )
    search_fields = ('name', 'country', 'city')
    ordering = ('name', 'country', 'city')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="60" ')

    get_image.short_description = 'аватар'
