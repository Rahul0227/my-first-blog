from django.shortcuts import render
from django.http import HttpResponse
#from first_app.models import Topic,Webpage,AccesRecord

# Create your views here.
def index(request):
    #my_dict = {'insert_me':"now i am coming from first_app/index.html!"}
    return render(request,'index.html',{'name':'rahul'})

def add(request):
    val1 = int(request.POST.get["num1"])
    val2 = int(request.POST.get["num2"])
    res = val1 + val2

    return render(request,"result.html", {'result':res})

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
