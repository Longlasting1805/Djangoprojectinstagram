
from django.conf.urls.static import static
from django.urls import path

from djangoProjectInstgram import settings
from instagram.views import index

urlpatterns = [
    path('', index, ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
