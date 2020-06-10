from django.shortcuts import render,redirect

from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import uploaded_files
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UploadForm
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

#Deletes file from database at pre delete signal
@receiver(pre_delete, sender=uploaded_files)
def mymodel_delete(sender, instance, **kwargs):
    instance.uploadedfile.delete(False)

def index(request):
    return render(request,"send_itdude/index.html",locals())
def base(request):
    return render(request,"send_itdude/base.html",locals())
def sent_succesfully(request,upload):
    return render(request,"send_itdude/sent_success.html",context={'upload':upload})



#Create User
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("its good")
            return redirect('send')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
#uploads file
def upload(request):
    
    if request.method == 'POST':
        
        form = UploadForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            uploaded=form.save(commit=False)
            uploaded.uploaded_by=request.user
            uploaded.save()
            
            return redirect('success',uploaded.uploadedfile.url)
    else:
        form = UploadForm()
    return render(request, 'send_itdude/send.html', {
        'form': form
    })

#Display instances of uploaded_files
class FilesListView(LoginRequiredMixin,ListView):
    
        model = uploaded_files
        template_name = 'send_itdude/upload_list.html'
        context_object_name = 'allfiles'

#Delete file 
def delete_file(request, pk):
    if request.method == 'POST':
        filetobedeleted = uploaded_files.objects.get(pk=pk)
        filetobedeleted.delete()
    return redirect('uploaded_files_list')




