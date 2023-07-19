from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Question(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 10000)
    content = models.TextField(null= True, blank= True)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.user.username} - Question'
    
    def get_absolute_url(self):
        return reverse('stackbase:question-detail', kwargs={'pk':self.pk})


    
