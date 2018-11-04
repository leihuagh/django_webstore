from django.urls import path

from . import views


app_name = 'delivery_panel'

urlpatterns = [

    # Delivery
    path('list/', views.DeliveryListView.as_view(),
         name='delivery-list'),

    path('update/<pk>', views.DeliveryUpdateView.as_view(),
         name='delivery-update'),

]