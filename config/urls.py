from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('calculator/', include('calculator.urls')),
]
