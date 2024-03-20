from django.urls import path

from dogs import views

app_name = 'dogs'

urlpatterns = [
    path('', views.dogs, name='index'),
    path('appearance/<slug:dog_slug>/', views.appearance, name='appearance'),
    path('care/<slug:dog_slug>/', views.care, name='care'),
    path('character/<slug:dog_slug>/', views.character, name='character'),
    path('illness/<slug:dog_slug>/', views.illness, name='illness'),
]
