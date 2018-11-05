#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse


class LessonLine(object):
    model = Lesson
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    style_fields = {'detail': 'ueditor'}
    # 修改icon图标
    model_icon = 'fa fa-superpowers'
    # 排序字段
    ordering = ['click_nums']
    # 字段更改为只读
    readonly_fields = ['click_nums']
    # 不显示字段
    exclude = ['fav_nums']
    # 在一个model中管理另一个model
    inlines = [LessonLine]
    # 在列表直接修改
    list_editable = ['degree', 'desc']

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)