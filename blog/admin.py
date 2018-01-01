from django.contrib import admin

from .models import Article

# 注册方式二
class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','content','pub_time')
	list_filter=('pub_time',)

admin.site.register(Article,ArticleAdmin)

# Register your models here.
# 注册方式一
# admin.site.register(Article)
