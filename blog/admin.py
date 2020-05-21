from django.contrib import admin
from .models import Post, Comment

#admin.site.register(Comment)
#admin.site.register(Social)

from .forms import PostForm

@admin.register(Post)
class FooModelAdmin(admin.ModelAdmin):
    form = PostForm
    fields = ('title', 'title_image', 'content', 'tags',)