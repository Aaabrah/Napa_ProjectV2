from django.contrib import admin
from .models import Users, StudentsModel, TeacherDirectionsModel, TeachersModel



@admin.register(Users)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name']
    list_display_links = ['id', 'get_full_name']
    list_filter = ['id']
    search_fields = ['first_name', 'last_name']


@admin.register(StudentsModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'status']
    list_display_links = ['id', 'get_full_name']
    list_filter = ['status']
    search_fields = ['user']

@admin.register(TeachersModel)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name']
    list_display_links = ['id', 'get_full_name']
    search_fields = ['user']

@admin.register(TeacherDirectionsModel)
class TDModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id',  'name']
    search_fields = ['name']
