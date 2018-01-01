from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime

from . import models

# Create your views here.

def hello(request):
	return HttpResponse('<html>hello world</html>')

def current_datetime(request):
	now=datetime.datetime.now()
	html="<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request,offset):
   try:  
       offset = int(offset)
   except ValueError:  
       raise Http404()  
   dt= datetime.datetime.now() + datetime.timedelta(hours=offset)
   html = "<html><body>In %s hour(s), it will be%s.</body></html>" % (offset, dt)  
   return HttpResponse(html)

def index(request):
	# return render(request,'blog/index.html',{'hello':'xixi'})

	# article=models.Article.objects.get(pk=1)
	# return render(request,'blog/index.html',{'article':article})

	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})



def article_page(request,article_id):
	article=models.Article.objects.get(pk=article_id)
	return render(request,'blog/article_page.html',{'article':article})


# def edit_page(request):
# 	return render(request,'blog/edit_page.html')

def edit_page(request,article_id):
	if str(article_id)=='0':
		return render(request,'blog/edit_page.html')
	article=models.Article.objects.get(pk=article_id)
	return render(request,'blog/edit_page.html',{'article':article})
	

	


# def edit_action(request):
# 	title=request.POST.get('title','Title')
# 	content=request.POST.get('content','CONTENT')
# 	models.Article.objects.create(title=title,content=content)
# 	articles=models.Article.objects.all()
# 	return render(request,'blog/index.html',{'articles':articles})

def edit_action(request):
	title=request.POST.get('title','Title')
	content=request.POST.get('content','CONTENT')
	article_id=request.POST.get('article_id','0')
	if article_id=='0':
		models.Article.objects.create(title=title,content=content)
		articles=models.Article.objects.all()
		return render(request,'blog/index.html',{'articles':articles})

	article=models.Article.objects.get(pk=article_id)
	article.title=title
	article.content=content
	article.save()
	return render(request,'blog/article_page.html',{'article':article})
