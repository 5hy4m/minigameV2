from django.urls import path
from . import views



app_name = 'mini_app'

urlpatterns = [
    path('fromhome',views.home,name = 'fromhome'),
    # path('bestScore/',views.archery_game,name = 'bestScore'),
    path('archery/',views.archery_game,name='archery'),
    path('tictactoe/',views.tictactoe,name= 'tictactoe'),
    path('fingercut/',views.fingercut,name = 'fingercut'),
    path('snakeattack/',views.snakeattack,name = 'snakeattack'),
    path('light_game/',views.light_game,name = 'light_game'),
    path('orbitshooter/',views.orbitshooter,name = 'orbitshooter'),
    path('feedback/',views.feedback,name = 'feedback')
]
