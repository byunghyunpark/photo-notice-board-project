from django import forms
from django.contrib.auth import password_validation

from .models import MyUser


class SignupModelForm(forms.ModelForm):

    # cleaned_date를 위해 별도 선언함
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = MyUser
        fields = (
            'email',
            # 순서지정을 위해 삽입함
            'password1',
            'password2',
            'last_name',
            'first_name',
            'phone_number',
            'nickname',
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # 비밀번호 1,2 일치여부 확인 & 비밀번호 유효성검사
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password2'],
            self.instance
        )
        return password2

    # 검증된 비밀번호로 유저 생성
    def save(self, *args, **kwargs):
        # superclass에서 save를 가져옴 db 저장은 아직 안함
        user = super(SignupModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        user.save()
        return user
