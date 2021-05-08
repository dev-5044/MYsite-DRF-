from django.contrib import admin
from orders.models import Order, Category, SubCategory, Image, Comment
from django.utils.safestring import mark_safe


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['name', 'user', 'category', 'sub_category', 'get_image']

    def get_image(self, obj):
        view = ' '.join(
            [f'<p><img src={img.image.url} width="60"></p>' for img in obj.image.all()]
            )
        return mark_safe(view)

    get_image.short_description = 'фото'


admin.site.register(Image)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Comment)
