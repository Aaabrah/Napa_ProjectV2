from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import CoursesModel, CategoriesModel, GroupsModel
from django.views.generic import DetailView, ListView, View


class CoursesModelView(ListView):
    template_name = 'courses.html'
    model = CoursesModel
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = CoursesModel.objects.all()
        return context


def CategoriesView(request):
    categories = CategoriesModel.objects.all()
    return render(request, 'courses.html', {'categories': categories})


def CoursesView(request, category_id):
    courses = CoursesModel.objects.filter(category=category_id)
    return render(request, 'courses.html', {'courses': courses})


class CourseDetailView(View):

    def get(self, request, pk):
        course = CoursesModel.objects.get(id=pk)
        return render(request, 'course-detail.html', {'course': course})


class GroupModelView(ListView):
    template_name = 'groups.html'
    model = CoursesModel
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = GroupsModel.objects.all()
        return context
