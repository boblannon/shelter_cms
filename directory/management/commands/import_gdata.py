from django.core.management.base import BaseCommand
from django.db import transaction

from directory.management.base.importer import GDATAImporter

class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **options):

        i = GDATAImporter()
        i.find_spreadsheet('Master Resource List')
        i.select_worksheet()
        i.get_data()
        i.save_json_data()
        i.upload()
