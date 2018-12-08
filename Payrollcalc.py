#collection of related methods(function inside a class)
#  and variables
# object- instance of a class
# constructor- first method that runs when a class is instantiated

class Payrollcalc:

    grossSalary = 0
    nssf = 0
    nhif= 0
    paye= 0
    benefits= 0
    #constructor

    def __init__(self, basic, house, over, other):
        self.grossSalary = int (basic) + int(house) + int(over) + int (other)
        self.benefits = int(house) + int (over) + int (other)
        self.getPaye()
        self.getNhif()
        self.getNssf()
        # self.getBenefits()

    # def getBenefits(self, house, over, other):
    #     self.benefits = int(house) + int (over) + int (other)


    def getNhif(self):
        if self.grossSalary < 6000:
            numnhif = 150
        elif self.grossSalary >= 6000 and self.grossSalary < 7999:
            numnhif = 300
        elif self.grossSalary >= 8000 and self.grossSalary < 11999:
            numnhif = 400
        elif self.grossSalary >= 12000 and self.grossSalary < 14999:
            numnhif = 500
        elif self.grossSalary >= 15000 and self.grossSalary < 19999:
            numnhif = 600
        elif self.grossSalary >= 20000 and self.grossSalary < 24999:
            numnhif = 750
        elif self.grossSalary >= 25000 and self.grossSalary < 29999:
            numnhif = 850
        elif self.grossSalary >= 30000 and self.grossSalary < 34999:
            numnhif = 900
        elif self.grossSalary >= 35000 and self.grossSalary < 39999:
            numhif = 950
        elif self.grossSalary >= 40000 and self.grossSalary < 44999:
            numnhifnhif = 1000
        elif self.grossSalary >= 45000 and self.grossSalary < 49999:
            numnhif = 1100
        elif self.grossSalary>= 50000 and self.grossSalary < 59999:
            numnhif = 1200
        elif self.grossSalary >= 60000 and self.grossSalary < 69999:
            numnhif = 1300
        elif self.grossSalary >= 70000 and self.grossSalary < 79999:
            numnhif = 1400
        elif self.grossSalary >= 80000 and self.grossSalary < 89999:
            numnhif= 1500
        elif self.grossSalary >= 90000 and self.grossSalary < 99999:
            numnhif= 1600
        elif self.grossSalary > 10000:
            numnhif = 1700
            self.nssf= numnhif

    def getPaye(self):
        if self.grossSalary <= 12298:
            numpaye = self.grossSalary * 0.1
        elif self.grossSalary >= 12299 and self.grossSalary < 23885:
            numpaye = self.grossSalary * 0.15
        elif self.grossSalary >= 23886 and self.grossSalary < 35472:
            numpaye = self.grossSalary * 0.2
        elif self.grossSalary >= 35473 and self.grossSalary < 47059:
            numpaye = self.grossSalary * 0.25
        elif self.grossSalary > 47059:
            numpaye = self.grossSalary * 0.3
            self.paye= numpaye

    def getNssf(self):
        if self.grossSalary <= 6000:
            numnssf = 6000 * 0.06
        elif self.grossSalary > 6000:
            numnssf =self.grossSalary * 0.1
            self.nssf= numnssf



