from django.db import models
import random
import string

def generate_session_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

class Session(models.Model):
    session_name = models.CharField(max_length=5, unique=True, default=generate_session_name)
    player_one_name = models.CharField(max_length=50, null=True, blank=True)
    player_two_name = models.CharField(max_length=50, null=True, blank=True)
    player_one_score = models.IntegerField(default=0)
    player_two_score = models.IntegerField(default=0)
    turn = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_full(self):
        return self.player_one_name is not None and self.player_two_name is not None
