from django import forms

from Petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add a comment ...'})
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name ... '
            }
        )
    )