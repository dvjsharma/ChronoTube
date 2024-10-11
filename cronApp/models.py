from django.db import models

class Video(models.Model):
    """
    Model representing a video with relevant metadata.
    
    Attributes:
        video_id (str): Unique identifier for the video, serving as the primary key.
        title: Title of the video.
        description: Detailed description of the video content.
        publishedAt: Date and time when the video was published.
        thumbnail_url: URL of the video's thumbnail image.
    """

    video_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publishedAt = models.DateTimeField()
    thumbnail_url = models.URLField()

    class Meta:
        """
        Meta options for the Video model.
        """
        # Index to optimize queries based on the publication date
        indexes = [
            models.Index(fields=['publishedAt']),
        ]

    def __str__(self):
        """
        String representation of the Video model.
        """
        return self.title
