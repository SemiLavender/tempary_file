# _*_ encoding: utf-8 _*_
__author__ = 'SemiLavender'
__date__ = '2019/3/5 11:09'

from .models import CityDist, CourseOrg, Teacher

import xadmin


class CityDistAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'points',
                    'add_time']
    search_fields = ['org', 'name', 'work_year', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'points']
    list_filter = ['org', 'name', 'work_year', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'points',
                   'add_time']


xadmin.site.register(CityDist, CityDistAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
