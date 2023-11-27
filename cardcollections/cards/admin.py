from django.contrib import admin
from .models import Company, League, Player, Nation, Team, Set, Subset, Card, Parallel

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'nation')

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'relase_date')

@admin.register(Subset)
class SubsetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'set')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('set', 'subset', 'player', 'team', 'number')

@admin.register(Parallel)
class CardAdmin(admin.ModelAdmin):
    list_display = ('subset', 'numbered', 'name')

# Puoi anche registrare altri modelli se ne hai

