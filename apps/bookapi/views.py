from django.shortcuts import render
from rest_framework.response import Response


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('GET',))
@renderer_classes((JSONRenderer, ))
def books(request):
    return Response(data={"books": [{"title": "clean code"}]})
