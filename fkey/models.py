from django.db import models

# Create your views here.
class employee(models.Model):
	ID=models.AutoField(primary_key=True)
	NAME=models.CharField(max_length=255,null=False,unique=True)
	SEX=models.CharField(max_length=10,null=False)

class salary(models.Model):
	SALARY=models.IntegerField(null=False)
	LEVEL=models.IntegerField(null=False)
	EMPLOYEE=models.ForeignKey("employee",on_delete=models.CASCADE)
	#调用其他App的models的方法
	#如果是新增加的，原来表里面已经有数据了，就需要null=True
	CONTACT=models.ForeignKey("book.contact",on_delete=models.CASCADE,null=True)

    