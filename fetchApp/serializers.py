from rest_framework import serializers
from cronApp.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model.

    This serializer converts Video model instances into JSON format and
    validates incoming data for creating or updating video records.
    """
    class Meta:
        model = Video
        fields = ['video_id', 'title', 'description', 'publishedAt', 'thumbnail_url']

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        This method is used to transform the Video instance into a dictionary
        format with camelCase keys, which is often preferred in JSON APIs.

        Returns:
            dict: A dictionary representation of the Video instance.
        """
        return {
            'videoId': self.instance.video_id,
            'title': self.instance.title,
            'description': self.instance.description,
            'publishedAt': self.instance.publishedAt,
            'thumbnailUrl': self.instance.thumbnail_url,
        }
