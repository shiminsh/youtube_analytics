import json
import requests
import urlparse
import datetime

from analytics.models import *
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

def home(request):
    return render_to_response('link.html', context_instance=RequestContext(request))

def linkgoogle(request):
    url = 'https://accounts.google.com/o/oauth2/auth?client_id='+settings.CLIENT_ID+'&redirect_uri=http://127.0.0.1:8000/oauth2callback&scope=https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/youtubepartner-channel-audit https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.force-ssl https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtubepartner&response_type=code&access_type=offline'
    return HttpResponseRedirect(url)

def callback(request):
    code = request.GET.get('code')
    print code
    payload = {'grant_type':'authorization_code', 'code':code,'client_id':settings.CLIENT_ID, 'client_secret':settings.CLIENT_SECRET, 'redirect_uri':'http://127.0.0.1:8000/oauth2callback'}
    response = requests.post('https://accounts.google.com/o/oauth2/token', data=payload)
    print response.text
    response = json.loads(response.text)
    print response
    access_token = response['access_token']
    #request.session['access_token'] = access_token
    print access_token
    today = datetime.datetime.today()
    past_two = today - datetime.timedelta(60)
    past_four = today - datetime.timedelta(120)
    past_lifetime = '1971-01-01'
    # response = requests.get('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=UCmokFxOysKH73pjudQGDfjQ&fields=items(contentDetails(relatedPlaylists))&access_token=%s' % access_token)
    # response = json.loads(response.text)
    # print response
    # response = urlparse.parse_qs(response.text)
    # print type(response)
    # print "channel list"
    response = requests.get('https://www.googleapis.com/youtube/v3/channels?part=id&mine=true&fields=items(id)&access_token=%s' % access_token)
    channel = str(json.loads(response.text)['items'][0]['id'])
    print channel, "channel_id"
    payload = {'ids':'channel==%s'% channel, 'start-date':past_two.strftime('%Y-%m-%d'), 'end-date':today.strftime('%Y-%m-%d'), 'metrics':'views', 'fields':'rows', 'access_token':access_token}
    response = requests.get('https://www.googleapis.com/youtube/analytics/v1/reports', params=payload)
    try:
        past_two_views = json.loads(response.text)['rows'][0][0]
    except:
        past_two_views = 0.0
    print past_two_views
    payload = {'ids':'channel==%s'% channel, 'start-date':past_four.strftime('%Y-%m-%d'), 'end-date':today.strftime('%Y-%m-%d'), 'metrics':'views', 'fields':'rows', 'access_token':access_token}
    response = requests.get('https://www.googleapis.com/youtube/analytics/v1/reports', params=payload)
    try:
        past_four_views = json.loads(response.text)['rows'][0][0]
    except:
        past_four_views = 0.0
    print past_four_views
    payload = {'ids':'channel==%s'% channel, 'start-date':past_lifetime, 'end-date':today.strftime('%Y-%m-%d'), 'metrics':'views', 'fields':'rows', 'access_token':access_token}
    response = requests.get('https://www.googleapis.com/youtube/analytics/v1/reports', params=payload)
    try:
        past_lifetime_views = json.loads(response.text)['rows'][0][0]
    except:
        past_lifetime_views = 0.0
    print past_lifetime_views
    response = requests.get('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=%s&fields=items(contentDetails(relatedPlaylists(uploads)))&access_token=%s' % (channel, access_token))
    upload_playlist = json.loads(response.text)['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print upload_playlist, "upload_playlist"
    result = {'Last 60 Days Views': past_two_views, 'Last 120 Days Views': past_four_views, 'Lifetime Avg Views': past_lifetime_views}
    return HttpResponse(json.dumps(result))


def channel_id(request):
    return render_to_response('channel.html', context_instance=RequestContext(request))

def authentication(request):
    channel = request.POST.get('channelId')
    request.session['channel'] = channel
    url = 'https://accounts.google.com/o/oauth2/auth?client_id='+settings.CLIENT_ID+'&redirect_uri=http://127.0.0.1:8000/posted&scope=https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/youtubepartner-channel-audit https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.force-ssl https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtubepartner&response_type=code&access_type=offline'
    return HttpResponseRedirect(url)

def info(request):
    code = request.GET.get('code')
    channel = request.session['channel']
    print code
    payload = {'grant_type':'authorization_code', 'code':code,'client_id':settings.CLIENT_ID, 'client_secret':settings.CLIENT_SECRET, 'redirect_uri':'http://127.0.0.1:8000/posted'}
    response = requests.post('https://accounts.google.com/o/oauth2/token', data=payload)
    print response.text
    response = json.loads(response.text)
    print response
    access_token = response['access_token']
    #request.session['access_token'] = access_token
    print access_token
    response = requests.get('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=%s&fields=items(contentDetails(relatedPlaylists(uploads)))&access_token=%s' % (channel, access_token))
    upload_playlist = json.loads(response.text)['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print upload_playlist, "Upload Playlist"
    response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId=%s&fields=items(contentDetails(videoId))&access_token=%s' % (upload_playlist, access_token))
    print json.loads(response.text)
    video_ids = []
    try:
        for x in json.loads(response.text)['items']:
            video_ids.append(str(x['contentDetails']['videoId']))
    except:
        pass
    video_list_string = ','.join(video_ids)
    print video_ids
    print video_list_string
    response = requests.get('https://www.googleapis.com/youtube/v3/videos?part=statistics&id=%s&fields=items(id,statistics(viewCount,likeCount))&access_token=%s' % (video_list_string, access_token))
    result = json.loads(response.text)
    print response.text
    print result
    return HttpResponse(json.dumps(result))

def details(request):
    subs = request.GET.get('subs', None)
    if not subs:
        subs = 400
    ch_details = ChannelDetails.objects.filter(subs_limit = True).exclude(subscriber__lte=subs)
    paginator = Paginator(ch_details, 25)

    page = request.GET.get('page')
    try:
        finals = paginator.page(page)
    except PageNotAnInteger:
        finals = paginator.page(1)
    except EmptyPage:
        finals = paginator.page(paginator.num_pages)
    data = serializers.serialize("json", finals)
    print data
    if request.is_ajax():
        return HttpResponse(data)
    else:
        return render_to_response('youtube_details.html',{'ch_details':ch_details, 'finals':finals, 'subs':subs}, context_instance=RequestContext(request))
