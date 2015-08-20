from django.core.management.base import BaseCommand, CommandError
from analytics.models import ChannelDetails
from analytics.parser import ParseChannel

class Command(BaseCommand):

    def handle(self, **options):
        obj = ParseChannel()
        e = True
        while e:
            obj.insert_details()
            obj.fetch_channels()
            e = obj.filldb_loop()