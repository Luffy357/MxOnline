#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

from .views import CourseListView
urlpatterns = [
    # 机构列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
]

