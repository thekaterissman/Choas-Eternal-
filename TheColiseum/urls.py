from django.contrib import admin
from django.urls import path
from game.views import play_game

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", play_game, name="play_game"),
]
