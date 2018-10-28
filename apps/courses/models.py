# -*- coding:utf8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher
# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name=u'课程名称')
    desc = models.TextField(max_length=500, verbose_name=u'课程描述')
    degree = models.CharField(choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')), max_length=10)
    teacher = models.ForeignKey(Teacher, verbose_name=u'授课讲师', null=True, blank=True)
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u'封面')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    category = models.CharField(max_length=20, verbose_name=u'课程类别', default=u'基础课程')
    tag = models.CharField(max_length=20, default='', verbose_name=u'标签')
    youneed_know = models.TextField(max_length=500, verbose_name=u'课程须知')
    teacher_tell = models.TextField(max_length=500, verbose_name=u'老师告诉你')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    # 获取章节数
    def get_zj_nums(self):
        return self.lesson_set.count()

    # 获取学习用户
    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    # 获取课程所有章节
    def get_course_lesson(self):
        return self.lesson_set.all()


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'视频')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    times = models.IntegerField(default=0, verbose_name=u'视频时长')
    url = models.CharField(max_length=200, verbose_name=u'访问地址', default='')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'资源名')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'资源文件', max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name