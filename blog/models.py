from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    views = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class ViewSite(models.Model):
    hostname = models.TextField(max_length=400)
    ip_address = models.TextField(max_length=400)

