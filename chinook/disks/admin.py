from django.contrib import admin

from .models import Album, Track, Artist

class TrackInLine(admin.TabularInline):
    model = Track
    extra= 5
class AlbumAdmin(admin.ModelAdmin):
   fieldsets = [
        (None, {"fields": ["title","artist"]}),
   ]
   inlines = [TrackInLine]
    
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)
admin.site.register(Artist)