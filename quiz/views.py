# quiz/views.py

from http.client import HTTPResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def quiz(request):
    r = HTTPResponse()
    return r

def question(request):
    if request.method == 'GET':
        data = {
            "id": 1,
            "text": "ประเทศไทยมีกี่จังหวัด",
            "choices": [50, 68, 72, 77]
        }
        return JsonResponse(data)


@csrf_exempt
def create_question(request):
    if request.method == 'POST' or request.method == 'GET':
        response_data = {
            "id":('id', 9),
            "text":('ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล'),
            "choices":('C','C++','C#','Python','R','Julia')
        }

        return JsonResponse(response_data, status=201)