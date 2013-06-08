# Create your views here.


from django.views.generic import DetailView, FormView, RedirectView, DeleteView, ListView, View
from django.http import HttpResponse, HttpResponseRedirect

from phone_application.phone_app.models import *
from phone_application.phone_app.forms import ProductForm

from django.shortcuts import redirect

from django.core import serializers


                
      
class IntegrateDatabase(View):      
     
   def get(self,request,*args,**kwargs):
     
      last_date = kwargs['last_date']
      data = serializers.serialize("json", Product.objects.filter(data_modyfikacji__gte=last_date)) 
            
      return HttpResponse(data, mimetype='application/json')
    
    
    
    
    
    
      
      
      