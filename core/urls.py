from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('dentalimplant/', views.dentalimplant, name='dental-implant'),
    path('treatments/', views.treatments, name ='treatments'),
    path('gallery/<int:pk>/', views.gallery_int, name='gallery-int'),
]
