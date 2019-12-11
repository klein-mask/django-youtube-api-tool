from django.contrib import admin

from app.models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title','id', )
	list_display_links = ('title',)


admin.site.register(Video, VideoAdmin)
