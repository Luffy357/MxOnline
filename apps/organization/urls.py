#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

from .views import OrgListView, AddUserAskView

urlpatterns = [
    # 机构列表页
    url(r'^list/', OrgListView.as_view(), name='org_list'),
    # 课程咨询
    url(r'^add_ask', AddUserAskView.as_view(), name="add_ask")

]