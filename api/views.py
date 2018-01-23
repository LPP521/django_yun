from django.shortcuts import render
from django.shortcuts import HttpResponse
from mpan.models import File
import json


def api_lixian(requests):
    dic = {}
    for a in list(File.objects.all()):
        dic[str(a._file_id)] = a._file_name
    return HttpResponse(json.dumps(dic), content_type='application/json; charset=utf-8')
