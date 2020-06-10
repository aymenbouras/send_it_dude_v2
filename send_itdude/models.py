from django.db import models

from django.contrib.auth import get_user_model
from .validators import validate_file_size


class uploaded_files(models.Model):
    user=get_user_model()
    uploaded_by = models.ForeignKey(user, on_delete=models.CASCADE,default="1")
    uploadedfile=models.FileField(validators=[validate_file_size])
    date_of_publish = models.DateTimeField(auto_now_add=True,verbose_name="Date of publish",null=True)
    
    def __str__(self):
        return self.uploadedfile.name
   
    





    

    


