from django.contrib import admin
from django.urls import path
from data_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<int:data_point_id>', views.delete_data, name='delete'),
    path('add/', views.add_data, name='add'),
    path('api/data/', views.manage_data_via_api, name='data_manage'),
    path('api/data/<int:pk>', views.delete_data_via_api, name='data_detail'),
]
