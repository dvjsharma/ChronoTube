from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publishedAt = models.DateTimeField()
    thumbnail_url = models.URLField()
    # Index for optimizing querying
    class Meta:
        indexes = [models.Index(fields=['publishedAt'])]
