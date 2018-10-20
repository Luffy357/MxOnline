#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 登录验证
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    # 注册验证
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})