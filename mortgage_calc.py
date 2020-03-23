class Installment():
    def __init__(self, no, principal, interest):
        self.no = no
        self.principal = principal
        self.interest = interest
        self.installment = principal + interest

    def __str__(self):
        return f'{self.no} {self.principal} {self.interest} {self.installment}'

class Calculator():
    def __init__(self, loan_amount, years, interest, is_decreasing):
        self.loan_amount = loan_amount
        self.years = years
        self.interest = interest
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
    k = int(input("Number of installments per year: "))
    interest = float(input("What is the interest rate (%)? ")) / 100
    installment = str(input("Equal or decreasing installments? (e/d) "))
    is_decreasing = installment == "d"
    commission = float(input("What is the commission fee(%)? ")) / 100
    commission_type = int(input(
        """Do you want to:
            1) Ignore commission fee
            2) Add commission fee to your credit payment
            3) Subtract commission fee from your credit payment
            4) Pay commission fee upfront
            (1/2/3/4): """))
    print(f"commission_type: {commission_type}")

    credit_payment = loan_amount
    fixed_fee = commission * loan_amount

    print(f"fixed fee: {fixed_fee}")
    if commission_type == 1:
        fixed_fee = 0
    elif commission_type == 2:
        loan_amount += fixed_fee
    elif commission_type == 3:
        credit_payment -= fixed_fee

    calc = Calculator(loan_amount, years, interest, is_decreasing)
    (installments, total_interest) = calc.calculate()
    for i in installments:
        print(str(i))
    print(total_interest)
