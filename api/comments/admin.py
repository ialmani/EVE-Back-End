from django.contrib import admin

# Register your models here.
from .models import Comment, ArticlesComment, VideosComment

admin.site.register(Comment)
admin.site.register(ArticlesComment)
admin.site.register(VideosComment)


