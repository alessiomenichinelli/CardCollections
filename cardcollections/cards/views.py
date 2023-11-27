from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import permissions, status

from .models import Company, League, Player, Nation, Team, Set, Subset, Card, Parallel
from .serializers import PlayerSerializer, TeamSerializer, SetSerializer, SubsetSerializer, CardSerializer, NationSerializer

class LoginAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'id': user.id, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class SetListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = SetSerializer

    def get_queryset(self):
        queryset = Set.objects.all()
        year = self.request.query_params.get('y', None)
        company = self.request.query_params.get('c', None)
        league = self.request.query_params.get('l', None)
        team = self.request.query_params.get('t', None)
        player = self.request.query_params.get('p', None)

        if year:
            queryset = queryset.filter(relase_date__year=year)
        if company:
            queryset = queryset.filter(company__name=company)
        if league:
            queryset = queryset.filter(leagues__name__in=[league])
        if player:
            queryset = queryset.filter(card__player = player).distinct()
        if team:
            queryset = queryset.filter(card__team = team).distinct()

        return queryset
    
class SetDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    lookup_field = 'id'

class SubsetListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubsetSerializer

    def get_queryset(self):
        queryset = Subset.objects.all()
        set = self.request.query_params.get('s', None)

        if set:
            queryset = queryset.filter(set=set)

        return queryset.order_by('-basic')
    
class SubsetDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subset.objects.all()
    serializer_class = SubsetSerializer
    lookup_field = 'id'


class CardListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.all().order_by('set','subset','number')
        player = self.request.query_params.get('p', None)
        team = self.request.query_params.get('t', None)
        set = self.request.query_params.get('s', None)

        if player:
            queryset = queryset.filter(player=player)
        if team:
            queryset = queryset.filter(team=team)
        if set:
            queryset = queryset.filter(set=set)

        return queryset

class CardDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = 'id'

class TeamListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all().order_by('name')
        nation = self.request.query_params.get('n', None)

        if nation:
            queryset = queryset.filter(nation__name=nation)
    
        return queryset
    
class TeamDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

class PlayerListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all().order_by('name')
    
        return queryset
    
class PlayerDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'id'

class NationListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NationSerializer

    def get_queryset(self):
        queryset = Nation.objects.all()    
        return queryset