from django.urls import path
from . import views
from . import authorization  # If you've kept the authorization functions in authorization.py
from django.urls import path
from .views import recommendation_view
from .views import audio_recognition_view

# If you've moved the authorization functions to views.py, you don't need this import

urlpatterns = [
    path('', views.main_page_view, name='main_page_view'),
    path('dashboard/', views.main_page_view, name='dashboard'),
    path('analyze/', views.analyze_image_view, name='analyze_image'),
    path('authorize/', views.authorize, name='authorize'),  # For initiating Spotify auth
    path('callback/', views.callback, name='callback'),    # For handling Spotify's response
    path('refresh_token/', views.refresh_token, name='refresh_token'),  # For refreshing the access token
    path('audio-recognition/', audio_recognition_view, name='audio_recognition_view'), # For audio recognition
    path('song-recognition/', views.song_recognition_view, name='song_recognition_view'), # For song recognition
    path('recommendation/', views.recommendation_view, name='recommendation_view'), # For recommendation
    path('top-charts/', views.top_charts_view, name='top_charts_view'), # For top charts
]