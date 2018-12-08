from peewee import *

try:
    db = PostgresqlDatabase('d5nesjke3clh9t', user= 'ofzbhyirapbzzn', host= 'ec2-54-235-133-42.compute-1.amazonaws.com', password= 'f619025b408cde3e3a4fe60d85c5ccf15e0fd7ad510b1bfefc7d82dd7ee49be4')
    print ('connection success')
except:
    print ('connection fail')

class Employee(Model):

    name = CharField('100')
    kra = CharField()
    houseallowance= FloatField()
    department = CharField()
    postion = CharField()
    basicsalary = FloatField()
    dob = DateField()

    class Meta:
        database = db #  This model uses the "payrollSystem.db" database.
        table_name_='employees'

Employee.create_table(fail_silently= True)
