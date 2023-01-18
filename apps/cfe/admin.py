from django.contrib import admin
from .models import Product, Color


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "price"
        # "sale_price",
        # "calc_discount"
    )
    list_editable = ("title", "price")


@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "rgb",
        "_hexa",
    )
    list_editable = ("rgb", "_hexa")
