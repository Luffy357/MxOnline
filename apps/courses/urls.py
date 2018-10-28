#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentView, AddCommentView, VideoPlayView
urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情列表
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    # 课程章节信息
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name='course_comment'),
    # 提交评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    # 视频播放
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),
]

