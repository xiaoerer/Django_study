from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns=[
	path('',views.hello,name='hello'),
	path('time/',views.current_datetime,name='current_datetime'),
	url(r'^time/(\d{1,2})$',views.hours_ahead,name='hours_ahead'),
	# url(r'^time/plus/(d{1,2})/$', 'blog.views.hours_ahead'),
	path('index/',views.index,name='index'),


	url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),

	# url(r'^edit/$',views.edit_page,name='edit_page'),
	url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
	url(r'^edit/action$',views.edit_action,name='edit_action'),
]