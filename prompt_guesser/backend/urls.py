from django.urls import path
from .views import *

urlpatterns = [
    path('sessions', CreateSessionView.as_view(), name='create_session'),
    path('sessions/list', ListSessionsView.as_view(), name='list_sessions'),
    path('sessions/<str:session_name>', GetSessionView.as_view(), name='get_session'),
    path('sessions/<str:session_name>/join', JoinSessionView.as_view(), name='join_session'),
    path('sessions/<str:session_name>/delete', DeleteSessionView.as_view(), name='delete_session'),

    path('sessions/<str:session_name>/status/player', PlayerStatusView.as_view(), name='player_status'),
    path('sessions/<str:session_name>/status/image', ImageStatusView.as_view(), name='image_status'),
    path('sessions/<str:session_name>/status/guess', GuessStatusView.as_view(), name='guess_status'),

    path('sessions/<str:session_name>/process-prompt', ProcessPrompt.as_view(), name='process_prompt'),
    path('sessions/<str:session_name>/process-guess', ProcessPromptGuesses.as_view(), name='process_guess'),

    path('sessions/<str:session_name>/end-turn', EndTurnView.as_view(), name='end_turn'),
]
