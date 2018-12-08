from employee import Employee
from flask import Flask,render_template, request, redirect, url_for

from flask import Flask
from payroll import Payroll
from Payrollcalc import Payrollcalc

app = Flask(__name__)

x=2

#create- POST, Read- GET, Update- POST, Delete- GET

@app.route("/")
def home():
    # Employee.create(name= 'Samson',
    #                 kra ='A000567M',
    #                 department='ICT',
    #                 postion='Developer',
    #                 basicsalary= 80000,
    #                 dob='3/1/2000')

    allemployees=  Employee.select()

    return render_template("index.html", displayemployees= allemployees)
#CALL THE FORM
@app.route ("/employee")
def employee():
    return render_template("addemployee.html")

@app.route ("/saveemployee", methods= ["POST"])
def saveEmployee():
    # name = request.form['form_name']
    # kra = request.form['form_kra']
    # department = request.form['form_department']
    # postion = request.form['form_postion']
    # basicsalary = request.form['form_basicsalary']
    # dob = request.form['form_dob']

    Employee.create(name= request.form['form_name'], kra = request.form['form_kra'], houseallowance= request.form['form_houseallowance'],
                    department=request.form['form_department'], postion=request.form['form_postion'],
                    basicsalary= request.form['form_basicsalary'], dob= request.form['form_dob'])

    allemployees = Employee.select()

    return redirect(url_for("home"))

@app.route ("/updateemployee/<id>", methods= ["POST"])
def updateEmployee(id):

    #fetch the employee using their id

    emp = Employee.select().where(Employee.id == int (id)).get()

    # update employee details

    emp.name = request.form['form_name']
    emp.kra = request.form['form_kra']
    emp.houseallowance = request.form ['form_houseallowance']
    emp.department = request.form['form_department']
    emp.postion = request.form['form_postion']
    emp.basicsalary = request.form['form_basicsalary']
    emp.dob = request.form['form_dob']
    emp.save()


    return redirect(url_for("home"))

@app.route ("/deleteemployee/<id>", methods= ["GET"])
def deleteEmployee(id):
    #fetch the employee using their id

    emp = Employee.select().where(Employee.id == int (id)).get()
    emp.delete_instance()
    return redirect(url_for("home"))


#payroll routes

@app.route("/payroll/<a>")
def payroll(a):
    allPayrolls = Payroll.select().join(Employee).where(Employee.id == int (a))

    return render_template("payroll.html", myPayrolls= allPayrolls, id= a)


@app.route("/payroll/add", methods= ["POST"])
def addPayroll():

    overtime = request.form['form_overtime']
    otherbenefits = request.form['form_otherbenefits']
    payrolldate = request.form['form_date']
    id = request.form['form_emp_id']

    emp= Employee.select().where(Employee.id == id).get()

    calc = Payrollcalc (emp.basicsalary, emp.houseallowance, overtime, otherbenefits)
    # calc2 = Payrollcalc.getBenefits (emp.houseallowance, overtime, otherbenefits)

    Payroll.create(
    benefits= calc.benefits,
    overtime = overtime,
    otherbenefits = otherbenefits,
    payrolldate = payrolldate,
    nhif= calc.nhif,
    nssf= calc.nssf,
    paye= calc.paye,
    employeeid = id
    )
    return redirect(url_for("payroll",a = id))




app.run
if __name__ =="__main__":
     app.run(debug=True, port=5005)




