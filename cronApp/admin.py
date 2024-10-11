from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Video model.
    """

    list_display = ('video_id', 'title', 'publishedAt', 'addedAt')
    search_fields = ('title', 'description')
    list_filter = ('publishedAt',)
    ordering = ('-publishedAt',)
    readonly_fields = ('addedAt',)


admin.site.register(Video, VideoAdmin)
