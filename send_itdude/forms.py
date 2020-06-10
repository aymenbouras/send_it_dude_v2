from django import forms
from .models import uploaded_files

from django.contrib.auth import get_user_model
class UploadForm(forms.ModelForm):
    
    
    class Meta:
        user=get_user_model()
    
        model = uploaded_files
        fields = ('uploadedfile',)
        
        
        
        