from django.urls import path
from .views import *


urlpatterns = [
    path('sessions', CreateSessionView.as_view(), name='create_session'),
    path('sessions/list', ListSessionsView.as_view(), name='list_sessions'),
    path('sessions/<str:session_name>', GetSessionView.as_view(), name='get_session'),
    path('sessions/<str:session_name>/join', JoinSessionView.as_view(), name='join_session'),
    path('sessions/<str:session_name>/delete', DeleteSessionView.as_view(), name='delete_session'),
    path('sessions/<str:session_name>/end_turn', EndTurnView.as_view(), name='end_turn')
]
