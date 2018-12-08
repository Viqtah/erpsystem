from peewee import *

try:
    db = PostgresqlDatabase('payrollSystem', user= 'postgres', host= 'localhost', password= 'Stima101')
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
