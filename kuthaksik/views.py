from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Haksik
import json

# Create your views here.

@csrf_exempt
def get_api_request(request):
    if request.method == "POST": # POST일 경우만 통과
        params_mealtime = json.loads(request.body)['action']['params']['mealtime'] # parameter에서 시간 받아옴

        try:
            today_haksik = Haksik.objects.latest('updated_at')
            
            if params_mealtime == 'breakfast':
                menu = today_haksik.breakfast.replace("\'", "\"")
                return JsonResponse(json.loads(menu))
            
            elif params_mealtime == 'lunch':
                menu = today_haksik.lunch.replace("\'", "\"")
                return JsonResponse(json.loads(menu))

            elif params_mealtime == 'dinner':
                menu = today_haksik.dinner.replace("\'", "\"")
                return JsonResponse(json.loads(menu))
        
        except Haksik.DoesNotExist:
            raise Http404()

    return HttpResponse(status=200)