from Payrollcalc import Payroll

personOne = Payroll(int (input("Enter Basic")), int (input("Enter House Allowance")), int (input("Enter OverTime")), int (input("Enter other Benefits")))


# calling one

personOne.getGross()

personOne.getBenefits()

personOne.getNhif()

personOne.getPaye()

personOne.getNssf()

personOne.getDedudctions()

personOne.getNetSalary()

print ("Your Total benefits are: ", personOne.benefits)
print ("Your Gross Income is: ", personOne.gross, "after")
print ("Your NHIF contribution is: ", personOne.nhif)
print ("Your PAYE contribution is: ", Payroll.paye)
print ("Your NSSF contribution is: ",Payroll.nssf)
print ("Your Total Deductions are: ",Payroll.deductions)
print ("Your Net Salary is: ",Payroll.net)