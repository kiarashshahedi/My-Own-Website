from django.contrib import admin
from django.urls import path

# import static and setting for loading static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', )
]

# loading static and media for development 
if settings.DEBUG:
    urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)