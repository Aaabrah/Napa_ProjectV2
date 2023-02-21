from django.contrib import admin

from courses.models import CoursesModel, GroupsModel, CategoriesModel


@admin.register(CoursesModel)
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title', 'price']
    list_filter = ['price']
    search_fields = ['title', 'description']


@admin.register(GroupsModel)
class GroupsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_student']
    list_display_links = ['id', 'name', 'number_student']
    list_filter = ['id']
    search_fields = ['name']


@admin.register(CategoriesModel)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
