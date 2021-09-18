from django.urls import path, include
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.how_to, name='how_to'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('summernote/', include('django_summernote.urls')),
]

