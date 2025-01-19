from django.db import models
import random
import string
from django.contrib.postgres.fields import ArrayField

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
    prompt = models.CharField(max_length=200, null=True, blank=True)
    prompt_guess = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.CharField(max_length=8000, blank=True, null=True)
    selected_image_url = models.CharField(max_length=8000, blank=True, null=True)
    styled_prompt = models.CharField(max_length=200, null=True, blank=True)
    styled_prompt_guess = models.CharField(max_length=200, null=True, blank=True)

    def is_full(self):
        return self.player_one_name is not None and self.player_two_name is not None
