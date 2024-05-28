from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelA, ModelB
from .utils import get_related_fields

def related_fields_view(request, model_a_id):
    model_a_instance = ModelA.objects.get(id=model_a_id)
    related_fields = get_related_fields(model_a_instance, ModelB)

    context = {
        'model_a': model_a_instance,
        'related_fields': related_fields,
    }

    return render(request, 'index.html', context)
