from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import start_fetch_task, stop_fetch_task

@api_view(['POST'])
def start_fetching(request):
    # get query form query params
    query = request.data.get('query')
    if not query:
        return Response({"error": "Query parameter is required."}, status=400)
    start_fetch_task(query)
    return Response({"message": f"Fetching started for query: {query}"})

@api_view(['POST'])
def stop_fetching(request):
    stop_fetch_task()
    return Response({"message": "Fetching stopped."})