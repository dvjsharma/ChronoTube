from rest_framework import serializers
from cronApp.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'title', 'description', 'publishedAt', 'thumbnail_url']

    def to_dict(self):
        """
        Convert the model instance to a dictionary
        """
        return {
            'videoId': self.instance.video_id,
            'title': self.instance.title,
            'description': self.instance.description,
            'publishedAt': self.instance.publishedAt,
            'thumbnailUrl': self.instance.thumbnail_url,
        }
