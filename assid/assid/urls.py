from InhalerAid import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('readings/', views.welcome, name='welcome')
]
