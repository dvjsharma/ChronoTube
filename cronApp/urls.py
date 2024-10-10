from django.urls import path
import cronApp.views as cronApp

urlpatterns = [
    path('start/', cronApp.start_fetching, name='start_fetching'),
    path('stop/', cronApp.stop_fetching, name='stop_fetching'),
]