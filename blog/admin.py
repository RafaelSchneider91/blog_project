from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin
# from .models import SomeModel

# Register your models here.

# admin.site.register(Article)  

# Apply summernote to all TextField in model.
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Article, ArticleAdmin)
