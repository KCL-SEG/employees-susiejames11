"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, commission_type, monthly_salary, hourly_salary, bonus_commission, commission_per_contract,
                 number_hours, number_contracts):
        self.name = name
        self.commission = commission_type
        self.salary = salary_type
        self.monthly_salary = monthly_salary
        self.hourly_salary = hourly_salary
        self.bonus_commission = bonus_commission
        self.commission_per_contract = commission_per_contract
        self.hours_worked = number_hours
        self.number_contracts = number_contracts


    def get_pay(self):
        salary = 0
        if self.salary == "hourly":
            salary += (self.hours_worked * self.hourly_salary)
        elif self.salary == "monthly":
            salary += self.monthly_salary

        if self.commission == "fixed":
            salary += self.bonus_commission
        elif self.commission == "per contract":
            salary += (self.commission_per_contract * self.number_contracts)
        return salary

    def __str__(self):
        string = ""
        string += self.name + " "
        print(self.salary)
        if self.salary == "monthly":
            string += "works on a monthly salary of " + str(self.monthly_salary)
        elif self.salary == "hourly":
            string += "works on a contract of " + str(self.hours_worked) + " hours at " + str(self.hourly_salary )+ "/hour"

        if self.commission == "fixed":
            string += " and receives a bonus commission of " + str(self.bonus_commission) + "."
        elif self.commission == "per contract":
            string += " and receives a commission for " + str(self.number_contracts) + " contract(s) at " + \
                      str(self.commission_per_contract) + "/contract" + "."
        else:
            string += "."

        string += "  Their total pay is " + str(self.get_pay()) + "."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", "none", 4000, 0, 0, 0, 0, 0)
print(billie.get_pay())
print(str(billie))


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", "none", 0, 25, 0, 0, 100, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", "per contract", 3000, 0, 0, 200, 0, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", "per contract", 0, 25, 0, 220, 150, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", "fixed", 2000, 0, 1500, 0, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", "fixed", 0, 30, 600, 0, 120, 0)
