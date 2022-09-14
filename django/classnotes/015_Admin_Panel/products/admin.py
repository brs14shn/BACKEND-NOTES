from django.contrib import admin


# Register your models here.
from .models import Product



class ProductAdmin(admin.ModelAdmin):
     list_display = ("name", "create_date", "is_in_stock", "update_date") 
     #! yönetici sayfasında hangi alanların görüneceği
     list_editable = ("name","is_in_stock",) 
     #! hangi alanların düzenlenebileceği içindir.
     list_display_links = ("create_date", )
     #! list_display'den en az bir öğe, düzenleme sayfasına bağlantı görevi görmelidir. bu öğe ayrıca list_editable içinde olamaz, aksi halde bir bağlantı işlevi göremez.
     list_filter = ("is_in_stock", "create_date")
     #search_fields = ("name",)
     prepopulated_fields = {'slug': ('name',)}
     list_per_page = 25
     date_hierarchy = "update_date"
     # fields = (('name', 'slug'), 'description', "is_in_stock")
     #* fields kullanılırsa fieldset kullanma 👇
     fieldsets = (
        (None, {
            "fields": (
                # to display multiple fields on the same line, wrap those fields in their own tuple
                ('name', 'slug'), "is_in_stock"
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            # "classes": ("collapse", ),
            "fields": ("description", "categories", "product_image"),
            'description': "You can use this section for optionals settings"
        })
    )

admin.site.register(Product,ProductAdmin)
# admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"