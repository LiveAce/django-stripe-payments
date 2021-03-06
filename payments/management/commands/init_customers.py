from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

from payments.models import Customer


class Command(BaseCommand):
    
    help = "Create customer objects for existing users that don't have one"
    
    def handle(self, *args, **options):
        for user in User.objects.filter(customer__isnull=True).exclude(username__startswith='BOT').exclude(username__startswith='HAL'):
            Customer.create(user=user)
            print "Created customer for %s" % user.email
