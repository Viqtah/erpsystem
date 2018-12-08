from peewee import *
from employee import Employee
from employee import db


class Payroll(Model):
    benefits = FloatField()
    payrolldate= DateField()
    overtime = FloatField()
    otherbenefits = FloatField()
    nhif = FloatField()
    nssf = FloatField()
    paye= FloatField()
    employeeid = ForeignKeyField(Employee, to_field='id',on_delete= "cascade", on_update="cascade")

    class Meta:
        database = db # This model uses the "payrollSystem.db" database.
        table_name_='payrolls'

Payroll.create_table(fail_silently= True)