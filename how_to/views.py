from django.shortcuts import render
from django.http import HttpResponse
from .models import HTModel
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def how_to(request):

    posts = HTModel.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, "how_to.html", {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(HTModel, pk=pk) #this was Post > HTModel
    return render(request, 'post_detail.html', {'post': post})