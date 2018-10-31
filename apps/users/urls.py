#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UploadPwdView

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 修改头像
    url(r'^upload/image/$', UploadImageView.as_view(), name='uplaod_image'),
    # 个人中心修改密码
    url(r'^upload/pwd/$', UploadPwdView.as_view(), name='uplaod_pwd'),

    ]
