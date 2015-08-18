import re
import requests
import base64

from bs4 import BeautifulSoup
from analytics.models import *
from urlparse import urlparse

class ParseChannel:

    def __init__(self):
        self.homeUrl = "https://www.youtube.com"

    def initialize_db(self):
        data = requests.get(self.homeUrl)
        soup = BeautifulSoup(data.text)
        links = soup.find_all('a', href=re.compile('/channel/'))
        distinct_ids = []
        for link in set(link.get('href') for link in links):
            channel_id = str(link).lstrip('/channel/')
            distinct_ids.append(channel_id)
            print "Saving Channel Id -> " + channel_id
            obj = ChannelDetails(ch_id=channel_id)
            obj.save()

    def insert_details(self):
        status = ChannelDetails.objects.filter(status=False)
        for x in status:
            data = requests.get(str(x.about_url))
            soup = BeautifulSoup(data.text)
            image = soup.find('img', class_="channel-header-profile-image")
            print "img_url1 ->", str(image['src'])
            try:
                img_url = 'https:' + str(image['src'])
                print "img_url ->", img_url
                response = requests.get(img_url)
                img_url = base64.b64encode(response.content)
            except:
                img_url = str(image['src'])
                print "img_url ->", img_url
                response = requests.get(img_url)
                img_url = base64.b64encode(response.content)
            name = soup.find('a', class_="branded-page-header-title-link")
            name = name.string
            stats = soup.find_all('span', class_="about-stat")
            subscriber = 0
            if len(stats) > 1:
                subscriber = "".join(str(stats[0].b.string).split(","))
                if int(subscriber) > 400:
                    x.subs_limit = True
            date = stats[-1].string
            views = 0
            if len(stats) > 2:
                views = "".join(str(stats[1].b.string).split(","))
            links = soup.find_all('a', class_="about-channel-link")
            twit_link = None
            fb_link = None
            for link in links:
                try:
                    if 'Twitter' in str(link['title']):
                        print "twit-> ", str(link['href'])
                        twit_link = str(link['href'])
                except:
                    pass
                try:
                    if 'Facebook' in str(link['title']):
                        print "fb_link-> ", str(link['href'])
                        fb_link = str(link['href'])
                except:
                    pass
            try:
                country = soup.find('span', class_="country-inline")
                country = str(country.string).strip()
            except:
                country = "others"
            print "country -------------->>>>>>>>>>" , country
            x.name = name
            x.pic = img_url
            x.views = views
            x.subscriber = subscriber
            x.fb_link = fb_link
            x.twitter_link = twit_link
            x.twitter_link = twit_link
            x.date_joined = date
            x.status = True
            x.country = country
            x.save()

    def fetch_channels(self):    
        fetched = ChannelDetails.objects.filter(fetched = False)
        for p in fetched:
            print "url", p.channels_url
            print "id-> " , p.ch_id
            data = requests.get(str(p.channels_url))
            soup = BeautifulSoup(data.text)
            links = soup.find_all('a', href=re.compile('/channel/'))
            distinct_ids = []
            for link in set(link.get('href') for link in links):
                parsed = urlparse(link)
                channel_id = str(parsed.path).lstrip('/channel/')
                channel_id = channel_id.split("/")
                if len(channel_id) == 1:
                    channel_id = channel_id[0]
                    distinct_ids.append(channel_id)
                    distinct_ids = list(set(distinct_ids))
            p.fetched = True
            p.save()
            for q in distinct_ids:
                try:
                    obj = ChannelDetails(ch_id=q)
                    obj.save()
                except:
                    pass
            
    
    def infinite_loop(self):
        status = ChannelDetails.objects.filter(status=False)
        fetched = ChannelDetails.objects.filter(fetched = False)
        if len(status) == 0 and len(fetched) == 0:
            return False
        else:
            return True

        



