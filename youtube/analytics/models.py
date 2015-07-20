from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class ChannelId(models.Model):
	channel_id = models.CharField(_('Channel Id'), max_length=40)

	def __unicode__(self):
		return self.name