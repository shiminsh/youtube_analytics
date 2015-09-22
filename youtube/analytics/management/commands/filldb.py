from django.core.management.base import BaseCommand, CommandError
from analytics.models import ChannelDetails
from analytics.parser import ParseChannel

class Command(BaseCommand):

    def handle(self, **options):
        obj = ParseChannel()
        e = True
        while e:
            while obj.insert_details():
                pass
            while obj.fetch_channels():
                pass
            e = obj.filldb_loop()