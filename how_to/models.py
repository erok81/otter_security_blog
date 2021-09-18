from django.conf import settings
from django.db import models
from django.utils import timezone

from django.urls import NoReverseMatch, reverse_lazy

class HTModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    summary = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='blog_images')
    created_date = models.DateTimeField(default=timezone.now)

# TODO add hashtags for seatching articls


    def get_absolute_url(self):
        return reverse_lazy('post_detail')

    class Meta:
        ordering = ('-created_date',)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'How to Post'


