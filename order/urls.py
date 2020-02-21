
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('checkout1/', views.Checkout1View.as_view(), name='checkout1'),
    path('checkout2/', views.Checkout2View.as_view(), name='checkout2'),
    path('to-checkout1/', views.ToCheckout1.as_view(), name='to-checkout1'),
    path('to-checkout2/', views.ToCheckout2.as_view(), name='to-checkout2'),
    # path('product/<int:pk>', views.CategoryDetail.as_view(), name='list'),
    # path('cart/', views.CartList.as_view(), name='cart'),
    # path('product/detail/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    # path('cart/add/', views.add_cart, name='add-cart'),
    # path('cart/delete-one/', views.cart_delete_one, name='cart-delete-one'),
    # path('cart/delete-all/', views.cart_delete_all, name='cart-delete-all'),
]