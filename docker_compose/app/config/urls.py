from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from movies.api.v1.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  home, name='home'),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('api/', include('movies.api.urls')),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
