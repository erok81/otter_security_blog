from django.shortcuts import render
from django.http import HttpResponse
from .models import HTModel
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def how_to(request):

    ht_posts = HTModel.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, "how_to.html", {'ht_posts': ht_posts})


def ht_post_detail(request, pk):

    ht_posts = get_object_or_404(HTModel, pk=pk) #this was Post > HTModel

    return render(request, 'ht_post_detail.html', {'ht_posts': ht_posts})
   