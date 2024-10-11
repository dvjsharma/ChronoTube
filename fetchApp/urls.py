from django.urls import path
import fetchApp.views as views

urlpatterns = [
    path('videos/', views.get_videos, name='get-videos'),
]
