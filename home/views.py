from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from how_to.models import HTModel
from walk_through.models import WKModel
from django.utils import timezone

def home(request):

    if request.method == 'GET':
        context = tweet_card()

        ht_posts = HTModel.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:5]
        wk_posts = WKModel.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:5]

    return render(request, 'home.html', {'context': context, 'ht_posts': ht_posts, 'wk_posts': wk_posts})

def tweet_card():
    
    consumer_key = 'yV3IcqIiqqz67kkzmiR81tCrM'
    consumer_secret = '5MJskrBmT8RsZm5F0ENwPurzPQ4WzWgyETF5w2Raih2f2dwjPW'
    access_key = '148624063-AEDIlTslSiWWmQWoclSQJ9ytAo2m9IICOSyakyyH'
    access_secret = 'vtGsBJUiwqlFwVSKny2if2RlMeFiFQISO0vibNOdFaski'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    tweets = api.search(q="cybersecurity", lang="en", count=5, result_type='popular')
    
    tweet_list = []
    for index,tweet in enumerate(tweets):
        tweet_dict = {}
        tweet_dict['username'] = '@' + tweets[index].user._json['screen_name'] + ':'
        tweet_dict['text'] = tweets[index].text
        tweet_dict['url'] = 'https://www.twitter.com/twitter/statuses/' + str(tweets[index].id)
                   
        tweet_list.append(tweet_dict)

    return tweet_list



