from django.urls import path
from . import views

urlpatterns = [
    path('set/<int:set_id>/', views.ChecklistGenSet.as_view(), name='set_cards_pdf'),
]