from django.db import models
from django.contrib.auth.models import User

from django.core.validators import FileExtensionValidator



    
def user_directory_path(request,filename):
    return f'{str(request.user)}/{filename}'

class Articles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.FileField(upload_to = user_directory_path, validators=[FileExtensionValidator( ['html'] )])
    title = models.CharField(max_length = 255, unique=True)

    def __str__(self):
        return self.title
