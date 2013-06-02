from django.core.management.base import BaseCommand
from django.db import transaction

from directory.management.base.importer import CSVImporter

class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **options):

        i = CSVImporter()
        i.upload()
