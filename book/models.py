from django.db import models

#如果需要将一个普通类变成一个可以映射数据库的ORM模型
#就必须将父类设置为models.Model或者他的子类
class book(models.Model):
	#图书ID，ini类型，自增长，不为空
	ID=models.AutoField(primary_key=True)
	#图书NAME,varchar(100),
	NAME=models.CharField(max_length=100,null=False,unique=True)
	#图书PRICE,float
	PRICE=models.FloatField(null=False,default=0)

	def __str__(self):				#print一个类的时候，会自动调用__str__方法
		name=self.NAME
		price=self.PRICE
		return "Book：《{name}》；Price：《{price}》".format(name=name,price=price)

class publisher(models.Model):
	#出版社NAME,varchar(100),
	NAME=models.CharField(max_length=100,null=False)
	#出版社ADDR,float
	ADDR=models.CharField(max_length=255,null=False)