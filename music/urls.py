from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('albums/', views.IndexViewA.as_view(), name='albums'),
    path('songs/', views.IndexViewS.as_view(), name='songs'),
    path('songs/<int:sid>', views.likes, name='likes'),
    path('albums/<int:pk>/', views.DetailViewA.as_view(), name='detail'),
    path('', views.search, name='home'),
]
