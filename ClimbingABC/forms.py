from django import forms
from .models import QuestionAnswer


class QuestionForm(forms.ModelForm):

    class Meta:
        model = QuestionAnswer
        fields = ('title', 'question', 'author',)
