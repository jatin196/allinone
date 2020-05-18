"""allinone URL Configuration
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('portfolio.urls')),
    path('blogs/', include('blogs.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns +=  path('__debug__/', include(debug_toolbar.urls)),

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

