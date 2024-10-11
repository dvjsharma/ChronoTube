from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .tasks import start_fetch_task, stop_fetch_task


def error_response(message, status_code):
    """
    Helper function to create a standardized error response.
    """
    return Response({"error": {"message": message, "code": status_code}}, status=status_code)


@api_view(['POST'])
def start_fetching(request):
    """
    Start fetching YouTube videos for the given query.
    """
    query = request.data.get('query', settings.DEFAULT_QUERY)

    try:
        start_fetch_task(query)
    except Exception as e:
        return error_response(f"Failed to start fetching: {str(e)}", 500)

    return Response({"message": f"Fetching started for query: {query}"})


@api_view(['POST'])
def stop_fetching(request):
    """
    Stop fetching YouTube videos.
    """
    try:
        stop_fetch_task()
    except Exception as e:
        return error_response(f"Failed to stop fetching: {str(e)}", 500)

    return Response({"message": "Fetching stopped."})
