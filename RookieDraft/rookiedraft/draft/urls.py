from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='draft-home'),
    path('draft/', views.draft, name='draft-room'),
    path('draft/<int:id>/', views.access, name='draft-room'),
    path('league/', views.find, name='searched-league'),
    path('league-list/<int:id>/', views.leaguelist, name='league-list'),
    path('save/<int:id>/', views.saveorder, name='save-draft-order'),
    path('view-only/<int:id>/', views.viewonly, name='view-only'),
]