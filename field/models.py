from django.db import models

#如果需要将一个普通类变成一个可以映射数据库的ORM模型
#就必须将父类设置为models.Model或者他的子类
class article(models.Model):
	#ID，Big int类型，自增长，不为空
	ID=models.BigAutoField(primary_key=True)
	#REMOVE，python中的布尔型对应mysql中的tinyint，要通过NullBooleanField设置是否可以为空，对应1/0
	#下面两种方式是相同的效果
	#REMOVE=models.NullBooleanField(default=False)
	REMOVE=models.BooleanField(default=False,null=True)
	#TITLE
	TITLE=models.CharField(max_length=255,null=True,unique=True)

class person(models.Model):
	NAME=models.CharField(max_length=255,null=False)
	EMAIL=models.EmailField()