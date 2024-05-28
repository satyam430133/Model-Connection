from django.db import models
from django.db.models import ForeignKey

def get_related_fields(instance, related_model):
    if not isinstance(instance, models.Model):
        raise ValueError("instance must be a Django model instance")

    related_fields = {}
    for field in related_model._meta.get_fields():
        if isinstance(field, ForeignKey) and field.related_model == type(instance):
            related_name = field.name
            related_objects = related_model.objects.filter(**{related_name: instance})
            related_fields[related_name] = related_objects

    return related_fields