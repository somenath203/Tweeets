from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_all_tweets, name='all_tweets'),
    path('tweet_create/', views.create_new_tweet, name='tweet_create'),
    path('tweet_edit/<int:tweet_id>/', views.edit_particular_tweet, name='tweet_edit'),
    path('tweet_delete/<int:tweet_id>/', views.delete_particular_tweet, name='tweet_delete'),
    path('register/', views.registerNewUser, name='register'),
] 