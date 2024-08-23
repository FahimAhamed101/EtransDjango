from django.contrib import admin
from .models import Category,banner,banneractive

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(banner)
admin.site.register(banneractive)