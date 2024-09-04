
# import static and setting for loading static files
from django.conf import settings
from django.conf.urls.static import static

# for api documentation 
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="TakKharid API Documentation",
      default_version='v1',
      description="API documentation",
      contact=openapi.Contact(email="OGODE..."),
   ),
   public=True,
)
urlpatterns = [
   path('admin/', admin.site.urls),
   # API urls
   path('accounts/', include('accounts.urls')),
   path('products/', include('products.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# loading static and media for development 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)