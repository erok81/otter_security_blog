from django.shortcuts import render
import tweepy
from how_to.models import HTModel
from walk_through.models import WKModel
from django.utils import timezone
from datetime import datetime
import os

def home(request):

    if request.method == 'GET':
        context = tweet_card()
        if context == None:
            context = [{'text':'twitter unavailable'},]
        else:
            pass

        ht_posts = HTModel.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:5]
        wk_posts = WKModel.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:5]
        ht_days = ht_diff_days()
        wk_days = wk_diff_days()

    return render(request, 'home.html', {'context': context, 'ht_posts': ht_posts, 'wk_posts': wk_posts, 'ht_days': ht_days, 'wk_days': wk_days})

def tweet_card():

    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    tweet_list = []

    try:
        tweets = api.search(q="cybersecurity", lang="en", count=5, result_type='popular')
    except:
        return
    
  
    for index,tweet in enumerate(tweets):
        tweet_dict = {}
        tweet_dict['username'] = '@' + tweets[index].user._json['screen_name'] + ':'
        tweet_dict['text'] = tweets[index].text
        tweet_dict['url'] = 'https://www.twitter.com/twitter/statuses/' + str(tweets[index].id)
                   
        tweet_list.append(tweet_dict)

    return tweet_list

def ht_diff_days():

    today = datetime.now(timezone.utc)
    last_created = HTModel.objects.all().last().created_date

    diff = abs(today - last_created).days

    if diff == 0:
        return 'today'
    elif diff == 1:
        return '1 day ago'
    else:
        return f'{diff} days ago'


def wk_diff_days():

    today = datetime.now(timezone.utc)
    last_created = WKModel.objects.all().last().created_date

    diff = abs(today - last_created).days

    if diff == 0:
        return 'today'
    elif diff == 1:
        return '1 day ago'
    else:
        return f'{diff} days ago'
        