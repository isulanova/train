from django.contrib import admin
from django.urls import path, include
from app import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('download/', include('main.urls', namespace='download')),
    path('find/', include('main.urls', namespace='find')),
    path('dogs/', include('dogs.urls', namespace='dogs')),
    path('user/', include('users.urls', namespace='user')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)