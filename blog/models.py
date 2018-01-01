from django.db import models

# Create your models here.
class Question(models.Model):
	"""docstring for Question"""
	# def __init__(self, arg):
	# 	super(Question, self).__init__()
	# 	self.arg = arg

	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
		
class Choice(models.Model):
	"""docstring for Choice"""
	# def __init__(self, arg):
	# 	super(Choice, self).__init__()
	# 	self.arg = arg

	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
		
# 建立数据模型 然后生成数据表
# 命令行中进入manage.py同级目录
# 执行python manage.py makemigrations app名（可选）
# 再执行python manage.py migrate
# django会自动在app/migrations/目录下生成移植文件

# 然后可以查看sql命令
# 执行python manage.py sqlmigrate 应用名 文件id查看sql语句
# python manage.py sqlmigrate blog 0002_article
class Article(models.Model):
	"""docstring for Article"""

	title=models.CharField(max_length=32,default='Title')
	content=models.TextField(null=True)
	# pub_time=models.DateTimeField(auto_now=True)
	pub_time=models.DateTimeField(null=True)

	def __str__(self):
		return self.title

		