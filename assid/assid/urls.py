from InhalerAid import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save_reading/', views.save_reading, name='save_reading'),
    path('', views.readings_table, name='readings_table'),
]
