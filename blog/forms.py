from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserForm(UserCreationForm):
    이메일 = forms.EmailField(required=True)  # 이메일 필드 추가
    이름 = forms.CharField(required=True)
    닉네임 = forms.CharField(required=True)
    전화번호 = forms.CharField(required=True)
    학번 = forms.CharField(required=True)
    성별 = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "이름", "닉네임", "전화번호", "학번", "성별", "이메일")


    def save(self, commit=True):  # 저장하는 부분 오버라이딩
        user = super(UserForm, self).save(commit=False)  # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["이메일"]
        user.realname = self.cleaned_data["이름"]
        user.nickname = self.cleaned_data["닉네임"]
        user.phone = self.cleaned_data["전화번호"]
        user.stdi = self.cleaned_data["학번"]
        user.gender = self.cleaned_data["성별"]
        if commit:
            user.save()
        return user