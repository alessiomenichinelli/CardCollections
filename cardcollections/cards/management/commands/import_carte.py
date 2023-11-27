# import_carte.py

import csv
from django.core.management.base import BaseCommand
from cards.models import Company, League, Player, Nation, Team, Set, Subset, Card

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
                set = Set.objects.get(code='SSA23')
                subset = Subset.objects.get_or_create(name=row['subset'], type='base', set=set)
                subset = Subset.objects.get(name=row['subset'], type='base', set=set)
                giocatore = Player.objects.get_or_create(name=row['giocatore'])
                giocatore = Player.objects.get(name=row['giocatore'])
                squadra = Team.objects.get(name=row['squadra'])
                numero = int(row['numero'])

                # Crea la carta nel database
                Card.objects.create(
                    set=set,
                    subset=subset,
                    player=giocatore,
                    team=squadra,
                    number=numero
                )

        self.stdout.write(self.style.SUCCESS('Importazione completata con successo'))
