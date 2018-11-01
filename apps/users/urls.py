#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UploadPwdView, SendEmailCodeView, UpdateEmailView

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 修改头像
    url(r'^upload/image/$', UploadImageView.as_view(), name='uplaod_image'),
    # 个人中心修改密码
    url(r'^upload/pwd/$', UploadPwdView.as_view(), name='uplaod_pwd'),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 发送邮箱验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),

    ]
