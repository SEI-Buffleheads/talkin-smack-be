from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    avatar = models.CharField(max_length=500)
    password = models.CharField(max_length=128)
    creation_date = models.DateTimeField()

    def __str__(self):
      return f'{self.first_name} - {self.username}'

    
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply')
    text = models.CharField(max_length=500)
    creation_date = models.DateTimeField()

    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.CharField(max_length=500)
    creation_date = models.DateTimeField()
    # reply_to = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='post', blank=True)
    
