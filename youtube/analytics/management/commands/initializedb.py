from django.core.management.base import BaseCommand, CommandError
from analytics.models import ChannelDetails
from analytics.parser import ParseChannel

class Command(BaseCommand):

    def handle(self, **options):
        details = ChannelDetails.objects.all()
        details.delete()
        obj = ParseChannel()
        obj.initialize_db()
        e = True
        while e:
            obj.insert_details()
            obj.fetch_channels()
            e = obj.infinite_loop()