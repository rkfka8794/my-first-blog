from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # 이메일 필드 추가
    name = forms.CharField(required=True)
    nickname = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    stid = forms.CharField(required=True)
    gender = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "name", "nickname", "phone", "stid", "gender", "email")


    def save(self, commit=True):  # 저장하는 부분 오버라이딩
        user = super(UserForm, self).save(commit=False)  # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        user.name = self.cleaned_data["name"]
        user.nickname = self.cleaned_data["nickname"]
        user.phone = self.cleaned_data["phone"]
        user.stdi = self.cleaned_data["stid"]
        user.gender = self.cleaned_data["gender"]
        if commit:
            user.save()
        return user