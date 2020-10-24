import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
"""django command to wait untill db is availbale"""

    def handelrs(self, *args, **opertions):
        self.stdout.write('Waiting for the data base....')
        db_conn = None 
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write("Databess is not returning anything...pleas wait")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('HERE YOU GO IT WORKED!!'))