from django.db import models
from django.utils.timezone import now


def get_curr_date():
    return now()


class CodePost(models.Model):
    title = models.CharField(max_length=150, default='Untitled')
    commentary = models.TextField(blank=True)
    author = models.CharField(max_length=150, default='Anonymous')
    body = models.TextField('maintext')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=get_curr_date)
