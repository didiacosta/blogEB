from django.contrib import admin
from .models import Post
# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ('id','title','content')
    search_fields = ('title',)

admin.site.register(Post, AdminPost)
