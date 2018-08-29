monthlyPayment = 0
remainder = balance
while remainder > 0:
    remainder = balance
    monthlyPayment += 10
    for _ in range(12):
        remainder -= monthlyPayment
        remainder += remainder * (annualInterestRate/12)
print(monthlyPayment)
