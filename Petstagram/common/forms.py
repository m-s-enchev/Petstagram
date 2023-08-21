from django import forms

from Petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.NumberInput(attrs={'placeholder': 'Enter a 10 digit number beginning with 0'})
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name ... '
            }
        )
    )