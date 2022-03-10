from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Every table is represented by the class Model in Django.
# in the models module you can find
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField() #unrestricted
  date_posted = models.DateTimeField(default=timezone.now)
  # The ForeignKey class means that : if User (author) is deleted -> their posts are deleted
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  
  def __str__(self):
    return '{} -> {}'.format(self.title,self.content) 
    
  