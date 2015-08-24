from django import forms
from django_comments.forms import CommentForm
from rating.models import CommentWithRating

class CommentFormWithRating(CommentForm):

    rating_option = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    rating  = forms.ChoiceField(choices=rating_option)

    def get_comment_model(self):
        # Use our custom comment model instead of the default one.
        return CommentWithRating

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the rating field
        data = super(CommentFormWithRating, self).get_comment_create_data()
        data['rating'] = self.cleaned_data['rating']
        return data
