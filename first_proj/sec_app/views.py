
from django.shortcuts import render
from django.http import HttpResponse
from sec_app.models import User
from .import forms
# Create your views here.
def index(request):
    return HttpResponse("<em>This is my First Project!!<em>")

def help(request):
    user_info=User.objects.order_by('first_name')
    fn={'access_records':user_info}
    return render(request,'help.html',context=fn)

def home(request):
    return render(request,'index.html')
    
def form_(request):
    form=forms.detail()

    if request.method=="POST":
        form=forms.detail(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!!!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request,'forms.html',{'form':form})

def contact(request):
    return HttpResponse("2345")
def contactuser(request):
    return HttpResponse("gy")