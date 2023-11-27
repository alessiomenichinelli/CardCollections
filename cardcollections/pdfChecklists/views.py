from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak, Spacer

from cards.models import Company, League, Player, Nation, Team, Set, Subset, Card, Parallel

class ChecklistGenSet(View):
    def get(self, request, set_id):

        set = get_object_or_404(Set, pk=set_id)

        subsets = Subset.objects.filter(set=set).order_by('-basic')

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{set.name}_cards.pdf"'

        buffer = response

        pdf = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            leftMargin=10,  # Imposta il margine sinistro a 20 unità
            rightMargin=10,  # Imposta il margine destro a 20 unità
            topMargin=10,  # Imposta il margine superiore a 20 unità
            bottomMargin=10,  # Imposta il margine inferiore a 20 unità
        )

        # Nella tabella ci stanno header + 40 celle

        tables = []

        double = True

        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 12),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.2, colors.gray),
        ])

        
        for k in range(len(subsets)):
            cards = Card.objects.filter(set=set, subset=subsets[k]).order_by('number')
            if k != len(subsets)-1:
                cards2 = Card.objects.filter(set=set, subset=subsets[k+1]).order_by('number')

            header = ['Subset', 'N.', 'Player', 'Team', 'Base']

            data = []

            parallels_obj = Parallel.objects.filter(subset=subsets[k]).order_by('-numbered')

            parallels = []

            for pp in parallels_obj:
                if pp.numbered not in parallels and pp.numbered:
                    parallels.append(pp.numbered)
             
            j = 0
            for pp in parallels:
                if j<11:
                    header.append(f'#/{pp}')
                    j += 1
            
            for card in cards:
                data.append([card.subset.name, card.number, card.player.name, card.team.name])

            n = len(cards) //40

            if n != 0:

                for i in range(n):

                    table = Table([header] + data[int(i*40):int((i+1)*40)])
                    table.setStyle(table_style)

                    table.hAlign = 'LEFT'

                    tables.append(table)
                    tables.append(PageBreak())

                if len(cards) % 40 != 0:

                    table = Table([header] + data[int((i+1)*40):])
                    table.setStyle(table_style)

                    table.hAlign = 'LEFT'

                    tables.append(table)
                    tables.append(PageBreak())
            else:
                table = Table([header] + data)
                table.setStyle(table_style)

                table.hAlign = 'LEFT'

                tables.append(table)
                if k != len(subsets)-1:
                    if len(cards) < 25 and len(cards2) < 35-len(cards) and double:
                        tables.append(Spacer(5,20))
                        double = False
                    else:
                        tables.append(PageBreak())
                        double = True

        tables.pop()
        pdf.build(tables)

        return response
