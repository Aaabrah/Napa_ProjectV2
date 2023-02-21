from django.db import models
from users.models import TeachersModel, StudentsModel


class CategoriesModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class CoursesModel(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, related_name='courses')
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class GroupsModel(models.Model):
    course = models.ForeignKey(CoursesModel, on_delete=models.RESTRICT, related_name='group')
    name = models.CharField(max_length=55)
    teacher = models.ForeignKey(TeachersModel, on_delete=models.RESTRICT, related_name='group')
    student = models.ManyToManyField(StudentsModel, related_name='group')
    number_student = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
