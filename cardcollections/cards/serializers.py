from rest_framework import serializers
from .models import Company, League, Player, Nation, Team, Set, Subset, Card

class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = ['id', 'name']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']

class TeamSerializer(serializers.ModelSerializer):
    nation = NationSerializer()
    class Meta:
        model = Team
        fields = ['id', 'name', 'nation']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name']

class SetSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    leagues = LeagueSerializer(many=True)

    class Meta:
        model = Set
        fields = ['id', 'name', 'code', 'company', 'leagues', 'relase_date']

class SubsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subset
        fields = ['id', 'name', 'type']

class CardSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    team = TeamSerializer()
    set = SetSerializer()
    subset = SubsetSerializer()

    class Meta:
        model = Card
        fields = ['id', 'set', 'subset', 'player', 'team', 'number']
