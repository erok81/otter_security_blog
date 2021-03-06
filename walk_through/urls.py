from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.walk_through, name='walk_through'),
    #url(r'summernote/', include('django_summernote.urls')),
    path('wk_post/<int:pk>/', views.wk_post_detail, name='wk_post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)