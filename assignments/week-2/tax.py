income = int(input('Enter your income: '))

if (income >= 0) and (income <= 1000):
    tax1 = (0.05*income)
    print(tax1)

elif (income > 1000) and (income <= 2000):
    tax2 = (0.05 * (income-1000)) +(0.1 * (income-1000))
    print(tax2)

elif (income > 2000):
    income3 = income-2000
    print(income3)
    income2 = income - income3 - 1000
    print(income2)
    income1 = income2
    print(income1)
    tax3 = (0.05 * (income1)) + (0.1 * (income2)) + (0.25 * income3)
    print(tax3)

else:
    print('Error')
