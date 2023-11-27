from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('card/', views.CardListAPIView.as_view(), name='card-list'),
    path('card/<int:id>/', views.CardDetailAPIView.as_view(), name='card-detail'),
    path('set/', views.SetListAPIView.as_view(), name='set-list'),
    path('set/<int:id>/', views.SetDetailAPIView.as_view(), name='set-detail'),
    path('subset/', views.SubsetListAPIView.as_view(), name='subset-list'),
    path('subset/<int:id>/', views.SubsetDetailAPIView.as_view(), name='subset-detail'),
    path('team/', views.TeamListAPIView.as_view(), name='team-list'),
    path('team/<int:id>/', views.TeamDetailAPIView.as_view(), name='team-detail'),
    path('player/', views.PlayerListAPIView.as_view(), name='player-list'),
    path('player/<int:id>/', views.PlayerDetailAPIView.as_view(), name='player-detail'),
    path('nation/', views.NationListAPIView.as_view(), name='nation-list'),
]
