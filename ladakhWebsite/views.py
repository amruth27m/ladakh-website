from django.shortcuts import render
from  django.http import HttpResponse
from  django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hello world')



def contactUs(request):
    return HttpResponse('Contact us')


def home(request):
    return render(request,'ladakhWebsite/index.html')

def testBulma(request):
    return render(request,'ladakhWebsite/testBulma.html')
