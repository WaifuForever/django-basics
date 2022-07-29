from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('bestMove', views.getBestMove),
    path('evaluate', views.testEvaluate),
    path('minimax', views.testMinimax),
    path('isComplete', views.testIsBoardComplete),
    path('isTerminal', views.testIsTerminal)
]