from django.urls import path, include
from django.contrib import admin
from .views import show_main, show_json, show_xml, show_json_by_id, show_xml_by_id, show_products, product_detail, add_product
from main.views import register, login_user
from main.views import logout_user
from .views import add_auction_season, place_bid
from .views import delete_product, edit_product
from . import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='show_main'),
    path('json/', show_json, name="show_json"),
    path('xml/', show_xml, name="show_xml"),
    path('json/<uuid:id>/', show_json_by_id, name="show_json_by_id"),
    path('xml/<uuid:id>/', show_xml_by_id, name="show_xml_by_id"),
    path('products/', show_products, name="show_products"),
    path('products/<uuid:id>/', product_detail, name="product_detail"),
    path('products/add/', add_product, name='add_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('seasons/add/', add_auction_season, name='add_season'),
    path('products/<uuid:id>/bid/', place_bid, name='place_bid'),
    path('products/<uuid:id>/edit/', edit_product, name='edit_product'),
    path('products/<uuid:id>/delete/', delete_product, name='delete_product'),
    path("products/partial/all/", views.all_products, name="products_all_partial"),
    path("products/partial/mine/", views.my_products, name="products_mine_partial"),
    path('profile/', views.profile, name='profile'),
    path('journal/', views.journal, name='journal'),
    path('my-bids/', views.my_bids, name='my_bids'),
    path("products/partial/", views.product_list_partial, name="product_list_partial"),
    path("api/products/add/", views.api_add_product, name="api_add_product"),
    path("api/products/<uuid:pk>/delete/", views.api_delete_product, name="api_delete_product"),
]