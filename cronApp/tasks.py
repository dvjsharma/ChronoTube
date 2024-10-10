import requests
import json
from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import datetime, timedelta
from cronApp.models import Video

YOUTUBE_API_KEYS = ['AIzaSyBGghhV_t4sdO5HgkOQqtm_4rlTC0x0VOc', 'YOUR_API_KEY2']

@shared_task
def fetch_latest_videos(query):
    api_key = YOUTUBE_API_KEYS[0]
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'order': 'date',
        'publishedAfter': (datetime.now() - timedelta(days=1)).isoformat("T") + 'Z',
        'key': api_key,
    }

    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data.get('items', []):
            video_data = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'publishedAt': item['snippet']['publishedAt'],
                'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
            }
            Video.objects.create(**video_data)

# Dynamically start the periodic task
def start_fetch_task(query):
    # Get or create a 10-second interval schedule
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS
    )
    # Create a periodic task for fetching videos
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Fetch YouTube videos for {query}',
        task='cronApp.tasks.fetch_latest_videos',
        args=json.dumps([query])
    )

# Stop the periodic task
def stop_fetch_task():
    PeriodicTask.objects.filter(task='cronApp.tasks.fetch_latest_videos').delete()
