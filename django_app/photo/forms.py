from django import forms

from .models import Photo, Album, Comment


class PhotoAdd(forms.Form):

    album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="필수선택")
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # 사진 없으면 error 출력
    file = forms.FileField(required=True)


class PhotoAddMulti(forms.Form):

    album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="필수선택")
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )
    )


class CommentAdd(forms.ModelForm):

    class Meta:
        model = Comment
        fields = {
            'content'
        }
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }


class PhotoEdit(forms.ModelForm):

    class Meta:
        model = Photo
        fields = {
            'title',
            'description',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }