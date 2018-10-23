# -*- coding:utf8 -*-
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from organization.models import CourseOrg, CityDict


class OrgListView(View):
    def get(self, request):
        all_org = CourseOrg.objects.all()
        all_city = CityDict.objects.all()

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
        })