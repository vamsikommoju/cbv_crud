from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,View,RedirectView
from app1.models import *
from app1.forms import *


# Create your views here.

# def index(request):
#     return render(request,'app1/index.html',{'msg':'This is Index Page'})

class home(TemplateView):
    template_name = 'app1/home.html'
    def get_context_data(self):
        data = {'msg':'this is home page'}
        return data
    

    def get_context_data(self):
        obj1 = Course.objects.all()
        form = Courseform()
        context = {'obj1':obj1,'form':form}
        return context
    
    def post(self,request):
        form = Courseform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
class update(View):
    def get(self,request,id):
        obj2 = Course.objects.get(pk=id)
        form = Courseform(instance=obj2)
        return render(request,'app1/update.html',{'form':form})
    
    def post(self,request):
        obj2 = Course.objects.get(pk=id)
        form = Courseform(request.POST,instance=obj2)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')      

class delete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args,**kwargs):
        id = kwargs['id']
        Course.objects.get(id=id).delete()
        return super().get_redirect_url(*args, **kwargs)

        



        

