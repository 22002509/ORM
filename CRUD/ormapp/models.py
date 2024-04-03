from django.db import models
class Employee (models. Model):
    empid=models. IntegerField()
    empname=models. CharField(max_length=20)
    dept=models. CharField(max_length=20)
    salary=models. FloatField()
    aadhaar=models. BigIntegerField(null=True)