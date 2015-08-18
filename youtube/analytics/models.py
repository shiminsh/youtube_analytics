from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class ChannelDetails(models.Model):
    ch_id = models.CharField(_('Channel Id'), max_length=40, unique=True)
    name = models.CharField(_('Channel Name'), max_length=100, blank=True, null=True)
    pic = models.TextField(_('Chanel Picture'), blank=True, null=True)
    views = models.IntegerField(_('Views'), max_length=100, default=0)
    subscriber = models.IntegerField(_('Subscriber'), max_length=100, default=0)
    fb_link = models.CharField(_('Facebook link'), max_length=250, blank=True, null=True)
    twitter_link = models.CharField(_('Twitter link'), max_length=250, blank=True, null=True)
    date_joined = models.CharField(_('Joined Date'), max_length=100, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=100, blank=True, null=True)
    status = models.BooleanField(default=False)
    fetched = models.BooleanField(default=False)
    subs_limit = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    @property
    def ch_url(self):
        url = "https://www.youtube.com/channel/" + str(self.ch_id)
        return url

    @property
    def about_url(self):
        ab_url = "https://www.youtube.com/channel/" + str(self.ch_id) + "/about"
        return ab_url

    @property
    def channels_url(self):
        chs_url = "https://www.youtube.com/channel/" + str(self.ch_id) + "/channels"
        return chs_url
