from django.shortcuts import render
from .models import article
from django.http import HttpResponse
# Create your views here.

def index(requset):
	a=article(REMOVE=True,TITLE='test01')
	a.save()
	return HttpResponse("正常")	
	