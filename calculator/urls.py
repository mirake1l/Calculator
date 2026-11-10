from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [path('<slug:model>/', views.calculator, name='calculate')]
