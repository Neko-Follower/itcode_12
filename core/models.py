from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=40)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    course = models.ManyToManyField(Course, verbose_name='Курсы')
