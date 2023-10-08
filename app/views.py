from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView,ListView
from app.form import *
from django.http import HttpResponse
# Create your views here
# TemplateView
class Temp(TemplateView):
    template_name='Temp.html'
    def get_context_data(self, **kwargs) :
        ECDO=super().get_context_data(**kwargs)
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Inserted Successfully!!!!')

# StudentInsertForm by using Form view
class StudentInsertForm(FormView):
    form_class=StudentForm
    template_name='StudentInsertForm.html'
    def form_valid(self,form):
        form.save()
        return HttpResponse('Data is insertted Successfully!!!')
    
# DisplayStudent by using ListView
class DisplayStudent(ListView):
    model=Student
    template_name='DisplayStudent.html'
    context_object_name='sclist'
    