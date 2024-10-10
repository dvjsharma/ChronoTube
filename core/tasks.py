import requests
from .models import Video
from celery import shared_task
from django.utils import timezone
from datetime import datetime

YOUTUBE_API_KEYS = ['haha', 'YOUR_API_KEY2']
QUERY = 'football'

@shared_task
def fetch_latest_videos():
    api_key = YOUTUBE_API_KEYS[0] 
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': QUERY,
        'type': 'video',
        'order': 'date',
        'publishedAfter': '2024-01-01T00:00:00Z',
        'key': api_key,
    }

    response = requests.get(search_url, params=params)
    data = response.json()
    for item in data['items']:
        video_data = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'publishedAt': item['snippet']['publishedAt'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
        }
        Video.objects.create(**video_data)

