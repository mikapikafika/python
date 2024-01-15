from django.contrib import admin
from django.urls import path
from data_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<int:data_point_id>', views.delete_data_point, name='delete'),
    path('add/', views.add_data_point, name='add'),
    path('api/data/', views.data_point_list, name='data_list'),
    path('api/data/<int:pk>', views.data_point_detail, name='data_detail'),
]
