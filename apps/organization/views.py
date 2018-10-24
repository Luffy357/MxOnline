# -*- coding:utf8 -*-
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

# Create your views here.
from organization.models import CourseOrg, CityDict
from .forms import UserAskForm


class OrgListView(View):
    def get(self, request):
        all_org = CourseOrg.objects.all()
        hot_orgs = all_org.order_by('-click_nums')[:3]

        all_city = CityDict.objects.all()

        # 对分页前的结果进行城市刷选
        city_id = request.GET.get('city', "")
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        # 类别刷选
        category = request.GET.get('ct', "")
        if category:
            all_org = all_org.filter(catgory=category)

        # 排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == 'students':
                all_org = all_org.order_by('students')
            elif sort == 'courses':
                all_org = all_org.order_by('course_nums')

        org_nums = all_org.count()

        # 实现分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, 2, request=request)

        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_org': orgs,
            'all_city': all_city,
            'org_nums': org_nums,
            'city_id': city_id,
            'hot_orgs': hot_orgs,
            'category': category,
            'sort': sort,
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg":"添加出错"}', content_type='application/json')