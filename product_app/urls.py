
from django.contrib import admin
from django.urls import path,include
from . views import add_product,view_all_product,delete_by_id,add_to_cart, delete_from_cart
#product/add_product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product/', add_product),
    path("view_all_products/",view_all_product),
    path('delete_by_id/<int:id>',delete_by_id,name="delete_by_id"),
    path("add_to_cart/<int:id>", add_to_cart, name="add_to_cart"),
    path("delete_from_cart/<int:cart_id>", delete_from_cart, name="delete_from_cart")
]
#http: