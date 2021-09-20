class Rental_property():

    def __init__(self, address):
        self.address = address
        self.income = 0
        self.expenses = 0
        

    def calc_income(self):
        rental_income = int(input("Enter your rental income"))
        more = input("Would you like to add info about laundry, storage or other things? <yes/no> ").lower()
        if more.lower() == 'yes':
            other = int(input("Enter additional income from other misc. "))
        elif more.lower() == 'no':
            other = 0
        additional_income = rental_income + other
        self.income +=additional_income 
    
    
    def calc_expenses(self):
        tax = int(input("Enter tax expenditure"))
        insurance = int(input("Enter isurance expenditure"))
        utilities = int(input("Enter utility expense"))
        morgage = int(input("Enter morgage"))
        hoa = int(input("Enter home owner association total fees. (Lawn care, vacancy, repairs, capital expenditures, ect."))
        additional_expenses = tax + insurance + utilities + morgage + hoa
        self.expenses += additional_expenses
        

    def cash_flow(self):
        self.cashflow = self.income - self.expenses


    def show_info(self):
        print(f"Address: {self.address} Income: {self.income} Expenses: {self.expenses} Cashflow: {self.cashflow}")
        



class User_interface():
    def __init__(self, rental_property):
        self.rental_property = rental_property
        

    def run(self):
        while True:
            self.rental_property.calc_income()
            self.rental_property.calc_expenses()
            self.rental_property.cash_flow()
            self.rental_property.show_info()

    
            

            
my_rental = Rental_property(input("Enter the address of the property you want to analyze."))
ui = User_interface(my_rental)
ui.run() 