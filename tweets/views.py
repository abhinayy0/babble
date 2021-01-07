from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from .form import TweetForm
from .models import Tweet


# Create your views here.

def homepage_view(request, *args, **kwargs):
    return render(request, "pages\home.html", context={}, status = 200)



def tweet_view(request, tweet_id, *args, **kwargs):

    data ={"id": tweet_id}
    #returning json data
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
        status = 200
    except:
        data['content'] = "Not found"
        status = 200
    return JsonResponse(data, status = status)


def all_tweets_view(request, *args, **kwargs):
    obj = Tweet.objects.all()
    all_tweets = [{'id': x.id, 'content': x.content, "likes": 123123 } for x in obj]
    data ={
        'response' : all_tweets
    }
    return JsonResponse(data)


def create_tweet_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid:
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()

    return render(request, 'components/form.html', context={"form": form})