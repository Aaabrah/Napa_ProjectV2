from django.urls import path
from .views import CategoriesView, CoursesView, CoursesModelView, GroupModelView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    path('', CoursesModelView.as_view(), name='all'),
    path('categories/', CategoriesView, name='categories'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('groups/', GroupModelView.as_view(), name='groups')
]
