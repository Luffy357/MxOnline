from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from organization.models import CourseOrg, CityDict


class OrgListView(View):
    def get(self, request):
        all_org = CourseOrg.objects.all()
        all_city = CityDict.objects.all()

        org_nums = all_org.count()

        return render(request, 'org-list.html', {
            'all_org': all_org,
            'all_city': all_city,
            'org_nums': org_nums,
        })