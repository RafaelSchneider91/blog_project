from django.db import models
# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(blank=True)

    def __str__(self):
        return self.title
