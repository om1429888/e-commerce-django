from django.contrib import admin
from .models import Product
from .models import Product_Variations
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','stock','category','modified_date','is_available')
    prepopulated_fields={'slug':('product_name',)}

class Product_VariationsAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active','created_date')
    list_editable=('is_active',)
    list_filter=('product','variation_category','variation_value','is_active','created_date')

admin.site.register(Product,ProductAdmin)
admin.site.register(Product_Variations,Product_VariationsAdmin)
