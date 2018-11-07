from django.db import models
#级表是固定的，员工表是员工信息，还有员工的联系方式表

class level(models.Model):
	LEVEL=models.IntegerField(null=False,primary_key=True,unique=True)
	SALARY=models.IntegerField(null=False)

class employee(models.Model):
	ID=models.AutoField(primary_key=True,unique=True)
	NAME=models.CharField(max_length=255,null=False)
	SEX=models.CharField(max_length=10,null=False)
	#外键，related_name用于引用
	LEVEL=models.ForeignKey("level",on_delete=models.CASCADE)	
	CONTACT=models.ForeignKey("contact",on_delete=models.CASCADE)

	def __str__(self):				#print一个类的时候，会自动调用__str__方法
		name=self.NAME
		level=self.LEVEL.LEVEL
		return "Name：{name}；Level：{level}".format(name=name,level=level)
		
class contact(models.Model):
	ADDR=models.TextField(null=True)
	NUM=models.CharField(max_length=255,null=True)


    