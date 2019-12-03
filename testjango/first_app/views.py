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
