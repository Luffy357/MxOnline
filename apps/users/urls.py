#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UploadPwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFvaOrgView, MyFavCourseView, MyMessageView

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

    # 我的课程
    url(r'^mycourses/$', MyCourseView.as_view(), name='mycourses'),

    # 我的收藏的机构
    url(r'^fav/org/$', MyFvaOrgView.as_view(), name='fav_org'),

    # 我的收藏的讲师
    url(r'^fav/teacher/$', MyFvaOrgView.as_view(), name='fav_teacher'),

    # 我的收藏的课程
    url(r'^fav/course/$', MyFavCourseView.as_view(), name='fav_course'),

    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),
    ]
