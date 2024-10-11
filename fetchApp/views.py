from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from django.db.models import Q
from fetchApp.serializers import VideoSerializer
from cronApp.models import Video
from django.urls import reverse

@api_view(['GET'])
def get_videos(request):
    query = request.GET.get('query', '')
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    sort_order = request.GET.get('sortOrder', 'desc')

    sort_field = '-publishedAt' if sort_order == 'desc' else 'publishedAt'
    
    videos = Video.objects.all()
    
    if query:
        search_terms = query.split()
        search_conditions = Q()
        for term in search_terms:
            search_conditions |= Q(title__icontains=term) | Q(description__icontains=term)

        videos = videos.filter(search_conditions)

        
    videos = videos.order_by(sort_field)
    paginator = Paginator(videos, limit)
    videos_page = paginator.get_page(page)
    
    serializer = VideoSerializer(videos_page, many=True)

    return Response({
        'total': paginator.count,
        'pages': paginator.num_pages,
        'videos': serializer.data,
        'next': (
            request.build_absolute_uri(
                reverse('get-videos') + f'?page={videos_page.next_page_number()}&limit={limit}&sortOrder={sort_order}'
                + (f'&query={query}' if query else '')
            ) if videos_page.has_next() else None
        ),
        'previous': (
            request.build_absolute_uri(
                reverse('get-videos') + f'?page={videos_page.previous_page_number()}&limit={limit}&sortOrder={sort_order}'
                + (f'&query={query}' if query else '')
            ) if videos_page.has_previous() else None
        ),
    })
