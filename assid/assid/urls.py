from InhalerAid import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('receive_data/', views.receive_data_view, name='receive_data'),
]
