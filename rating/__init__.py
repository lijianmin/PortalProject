from rating.models import CommentWithRating
from rating.forms import CommentFormWithRating

def get_model():
    return CommentWithRating

def get_form():
    return CommentFormWithRating
