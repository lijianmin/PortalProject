from django.db              import models
from django_comments.models import Comment

# Create your models here.
class CommentWithRating(Comment):

    rating = models.IntegerField(default=1)
