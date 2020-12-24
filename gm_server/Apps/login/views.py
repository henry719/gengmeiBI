from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from . import models
import json

# Create your views here.

def index(request):
    return HttpResponse("web")

@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        users = models.User.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

