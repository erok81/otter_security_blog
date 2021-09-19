from django.urls import path, include
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.how_to, name='how_to'),
    path('ht_post/<int:pk>/', views.ht_post_detail, name='ht_post_detail'),
    #path('summernote/', include('django_summernote.urls')),
]

