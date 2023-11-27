# import_carte.py

import csv
from django.core.management.base import BaseCommand
from cards.models import Company, League, Player, Nation, Team, Set, Subset, Card, Parallel

class Command(BaseCommand):
    help = 'Importa carte da un file CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Il percorso del file CSV')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r') as file_csv:
            csv_reader = csv.DictReader(file_csv)

            for row in csv_reader:
                # Converte i dati dalla stringa al tipo corretto
                set = Set.objects.get(codice="SSA23")
                subset = Subset.objects.get_or_create(name=row['subset'], type='base', set=set)
                subset = Subset.objects.get(name=row['subset'], type='base', set=set)
                name = row['name']
                if row['numbered'] != '':
                    numbered = int(row['numbered'])
                    

                    # Crea la carta nel database
                    Parallel.objects.create(
                        subset=subset,
                        numbered=numbered,
                        name=name,
                    )
                else:
                    Parallel.objects.create(
                        subset=subset,
                        name=name,
                    )
        self.stdout.write(self.style.SUCCESS('Importazione completata con successo'))
