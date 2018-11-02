from django.shortcuts import render
from .models import book
from django.http import HttpResponse

# Create your views here.
def input(request):
	book01=book(NAME="走走飘飘",PRICE=24.8)
	book01.save()
	return HttpResponse("图书录入成功!!")

def search(request):
	#根据主键查找表中数据
	sbook01=book.objects.get(pk=4)
	#根据列名查看数据，filter是过滤，匹配
	sbook02=book.objects.filter(NAME='飘')
	#删除数据
	#sbook03=book.objects.get(ID=9)
	#sbook03.delete()
	#修改数据
	sbook04=book.objects.get(NAME='飘过')
	sbook04.PRICE=9.9
	sbook04.save()
	return HttpResponse(sbook04)
