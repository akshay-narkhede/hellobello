from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

'''
def information(request):

    #tmp_var='f strings'
    #html_=f"""
    #<!DOCTYPE html>
    #<html>
    #<body>

    #<h1>HTML</h1>
    #<p>My first paragraph with {tmp_var}.</p>

    #</body>
    #</html>
    #"""
    #return HttpResponse(html_)

    return render(request,"information.html",{})
    #return HttpResponse("HELLO BELLO")
    #return render(request,"home.html",{})
    #return render(request,template,{dictionary})


def home(request):
    num=random.randint(0,100)
    context={
        "my_name":"AKSHAY",
        "num":num,
        "bool_item":True
        }
    return render(request,"home.html", context)
    #return render(request,template,{dictionary})


def about(request):
    return render(request,"about.html",{})

'''
#Class-based-Views
class AboutView(View):
    def get(self, request,*args,**kwargs):
        print(kwargs)
        return render(request,"about.html",{})

#TemplateViews
class HomeView(TemplateView):
    template_name="home.html"
    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        num=random.randint(0,100)
        context={
            "my_name":"AKSHAY",
            "num":num,
            "bool_item":True
            }
        print(context)
        return context

class InformationView(TemplateView):
    template_name="information.html"

class AboutTemplateView(TemplateView):
    template_name="about.html"
