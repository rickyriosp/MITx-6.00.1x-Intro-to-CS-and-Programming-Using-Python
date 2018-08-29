for _ in range(12):
    balance -= balance * monthlyPaymentRate
    balance += balance * (annualInterestRate/12)
print(round(balance, 2))
