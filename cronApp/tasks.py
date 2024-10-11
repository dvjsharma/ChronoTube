import requests
import json
from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import datetime, timedelta
from cronApp.models import Video
from django.db import IntegrityError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

YOUTUBE_API_KEYS = settings.YOUTUBE_API_KEYS
API_MAP = [
    {'key': key, 'last_used': 0, 'error_count': 0} 
    for key in YOUTUBE_API_KEYS
]
CURRENT_KEY_INDEX = 0

def get_videos_from_youtube(query):

    global CURRENT_KEY_INDEX  
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    for _ in range(len(API_MAP)):

        key = API_MAP[CURRENT_KEY_INDEX]['key']
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'order': 'date',
            'publishedAfter': (datetime.now() - timedelta(days=3)).isoformat("T") + 'Z',
            'key': key,
        }

        try:
            response = requests.get(search_url, params=params)
            if response.status_code == 200:
                API_MAP[CURRENT_KEY_INDEX]['last_used'] = datetime.now().timestamp()
                API_MAP[CURRENT_KEY_INDEX]['error_count'] = 0
                logger.info(f"API call successful with API key: {key}")
                return response.json().get('items', [])
            elif response.status_code == 403:
                API_MAP[CURRENT_KEY_INDEX]['error_count'] += 1
                logger.warning(f"API key exhausted: {key}")
            else:
                API_MAP[CURRENT_KEY_INDEX]['error_count'] += 1
                logger.error(f"Error fetching videos with API key: {key}: {e}")
        except Exception as e:
            API_MAP[CURRENT_KEY_INDEX]['error_count'] += 1
            logger.error(f"Error fetching videos with API key: {key}: {e}")


        CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(API_MAP)

    return []

@shared_task
def fetch_latest_videos(query):
    videos = get_videos_from_youtube(query)

    video_objects = []
    for item in videos:
        video_data = {
            'video_id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'publishedAt': item['snippet']['publishedAt'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
        }
        video_objects.append(Video(**video_data))

    try:
        Video.objects.bulk_create(video_objects, ignore_conflicts=True)
    except IntegrityError as e:
        logger.error(f"Error while saving videos: {e}")

def start_fetch_task(query):
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Fetch YouTube videos for {query}',
        task='cronApp.tasks.fetch_latest_videos',
        args=json.dumps([query])
    )

def stop_fetch_task():
    PeriodicTask.objects.filter(task='cronApp.tasks.fetch_latest_videos').delete()
