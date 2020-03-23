class Installment():
    def __init__(self, no, principal, interest):
        self.no = no
        self.principal = principal
        self.interest = interest
        self.installment = principal + interest

    def __str__(self):
        return f'{self.no} {self.principal} {self.interest} {self.installment}'

class Calculator():
    def __init__(self, loan_amount, years, interest, fixed_fee, is_decreasing):
        self.loan_amount = loan_amount
        self.years = years
        self.interest = interest
        self.fixed_fee = fixed_fee
        self.is_decreasing = is_decreasing

    def calc_equal(self):
        n = self.years * 12
        installment = (self.loan_amount * self.interest) \
                    / (12 * (1 - (12/(12 + self.interest)) ** n))
        print(installment)
        ratio = 1 + self.interest / n
        interest = (self.interest / 12) * self.loan_amount
        principal = installment - interest
        installments = [Installment(1, principal, interest)]
        for i in range(2, n+1):
            principal *= ratio
            interest = installment - principal
            installments.append(Installment(i, principal, interest))

        total_interest =  installment * n - self.loan_amount
        return (installments, total_interest)

    def calc_decreasing(self):
        pass

    def calculate(self):
        if self.is_decreasing:
            return self.calc_decreasing()
        else:
            return self.calc_equal()

if __name__ == "__main__":
    loan_amount = int(input("How much do you want to borrow? "))
    years = int(input("For how many years? "))
    interest = float(input("What is the interest rate (%)? ")) / 100
    installment = str(input("Equal or decreasing installments? (e/d) "))
    is_decreasing = installment == "d"

    calc = Calculator(loan_amount, years, interest, 0, is_decreasing)
    (installments, total_interest) = calc.calculate()
    for i in installments:
        print(str(i))
    print(total_interest)
