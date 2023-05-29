import django_filters as filters
from core import models


class UserSearch(filters.FilterSet):
    class Meta:
        model = models.User
        fields = ['group', ]
