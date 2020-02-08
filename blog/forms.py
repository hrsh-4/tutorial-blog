from django import forms
from .models import Post
import random
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields  = ['post_title','post_description','is_published','post_type']
# from allauth.account.forms import SignupForm
# from simplemathcaptcha.fields import MathCaptchaField
# from simplemathcaptcha.widgets import MathCaptchaWidget
#
# class MyCustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#
#         self.fields['captcha'] = MathCaptchaField(widget=MathCaptchaWidget(question_tmpl=('What is %(num1)i %(operator)s %(num2)i ? ')),
#     error_messages = {'invalid': ('Please check your math and try again.'), 'invalid_number': ('Enter a whole number.')})
#     def save(self, request):
#         captcha = self.cleaned_data.get('captcha')
#
#         user = super(MyCustomSignupForm, self).save(request)
# 
# class UserSearchForm(forms.ModelForm):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = 'user_username'
