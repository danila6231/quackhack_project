from django.urls import path
from .views import CreateSessionView, JoinSessionView, DeleteSessionView, ListSessionsView

urlpatterns = [
    path('sessions', CreateSessionView.as_view(), name='create_session'),
    path('sessions/list', ListSessionsView.as_view(), name='list_sessions'),
    path('sessions/<str:session_name>/join', JoinSessionView.as_view(), name='join_session'),
    path('sessions/<str:session_name>/delete', DeleteSessionView.as_view(), name='delete_session'),
]
