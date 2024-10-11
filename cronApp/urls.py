from django.urls import path
import cronApp.views as views

urlpatterns = [
    path('start/', views.start_fetching, name='start_fetching'),
    path('stop/', views.stop_fetching, name='stop_fetching'),
]
