from django.contrib import admin
from co.models import *
from django.contrib.auth.admin import GroupAdmin,UserAdmin
from django.contrib.auth.models import Permission,Group
from django.utils.translation import gettext_lazy as _

class MyUserAdmin(UserAdmin):
    list_display = ("username","first_name","last_name","email","is_active")
    search_fields = ('user__username',)
    list_per_page = 15

class UserInfoAdmin(admin.ModelAdmin):
    list_display =("user","phone","address","occupation","phone","tribe","age","empNo")
    search_fields = ('user__username',)
    list_per_page = 15

class MyGroupAdmin(GroupAdmin):
    list_display =("id","name")
    list_per_page = 15

class ProfileAdmin(admin.ModelAdmin):
    list_display =("User","image","date_updated")
    search_fields = ('User__username',)
    list_per_page = 15

class CaseAdmin(admin.ModelAdmin):
    list_display =("case_no","reporter","case_site","phoneNo","description","created_at","status")
    search_fields = ('case_no',)
    list_per_page = 15

class CaseAssignmentAdmin(admin.ModelAdmin):
    list_display =("user","case","date_assigned","is_active")
    search_fields = ('user__username',)
    list_per_page = 15

class CaseStatusAdmin(admin.ModelAdmin):
    list_display =("caseassignment","datetime","contact","description")
    search_fields = ('contact',)
    list_per_page = 15


class PermissionAdmin(admin.ModelAdmin):
    list_display =("name","codename")
    search_fields = ('name',)
    list_per_page = 15

admin.site.unregister(Group)
admin.site.register(Role, MyGroupAdmin)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(CaseAssignment, CaseAssignmentAdmin)
admin.site.register(CaseStatus, CaseStatusAdmin)

admin.site.site_url = '/homepage_url'