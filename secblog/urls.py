from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from codeify import views

urlpatterns = [
    path('otter-sec-admin/', admin.site.urls),
    path('how-to/', include('how_to.urls')),
    path('walkthrough/', include('walk_through.urls')),
    path('', include('home.urls')),
    path('coder/', views.codeify, name='codeify'),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)