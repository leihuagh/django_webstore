from django.urls import path

from . import views


app_name = 'users_panel'

urlpatterns = [
    path('staff-list', views.StaffListView.as_view(),
         name='staff-list'),

    path('client-list', views.ClientListView.as_view(),
         name='client-list'),

    path('user-bulk-action', views.UserBulkActionView.as_view(),
         name='user-bulk-action'),

    path('login', views.StaffLoginView.as_view(),
         name='login'),

    path('logout', views.StaffLogoutView.as_view(),
         name='logout'),

]
