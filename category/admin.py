from django.contrib import admin
from .models import Category,banner,banneractive,Category_Offer,bannertwo

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(banner)
admin.site.register(banneractive)
admin.site.register(bannertwo)
admin.site.register(Category_Offer)