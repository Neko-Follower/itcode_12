import factory
from faker import Factory
from core import models

factory_ru = Factory.create('ru-Ru')


class Group(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Group


class Course(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Course


class User(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    group = factory.SubFactory(Group)

    class Meta:
        model = models.User

    @factory.post_generation
    def course(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.course.add(extracted)