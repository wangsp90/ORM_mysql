from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from book.models import contact

def index(request):
	e01=employee(NAME="Mary",SEX="F")
	e01.save()

	con01=contact(ADDR="GZ",NUM="13888888888")
	con01.save()
	
	level01=salary(SALARY=3000,LEVEL=1)
	level01.EMPLOYEE=e01
	level01.CONTACT=con01
	level01.save()
	return HttpResponse("成功！")
