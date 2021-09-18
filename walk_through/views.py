from django.shortcuts import render
from django.http import HttpResponse
from .models import WKModel
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def walk_through(request):

    wk_posts = WKModel.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, "walkthrough.html", {'wk_posts': wk_posts})


def post_detail(request, pk):

    wk_posts = get_object_or_404(WKModel, pk=pk) #this was Post > HTModel

    return render(request, 'post_detail.html', {'wk_posts': wk_posts})
