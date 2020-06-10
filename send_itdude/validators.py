from django.core.exceptions import ValidationError


#Validate size valu less than 20mo
def validate_file_size(value):
    filesize= value.size
    
    if filesize > 20971520:
        raise ValidationError("The maximum file size that can be uploaded is 20MB")
    else:
        return value