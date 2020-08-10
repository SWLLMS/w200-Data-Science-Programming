a = int(input("Enter a number for A: "))
b = int(input("Enter a number for B: "))

math = int(input("""Enter the number 1 for arithmetic mean.
Enter the number 2 for geometric mean.
Enter the number 3 for root-mean-square: """))

if math == 1:
    a_mean = (a+b)/2
    print('The arithmetic mean is', a_mean)
elif math == 2:
    g_mean = (a*b)**0.5
    print('The geometric mean is', g_mean)
elif math == 3:
    r_mean = (((a**2)+(b**2))/2)**0.5
    print('The root-mean-square is', r_mean)
else:
    print('Invalid selection. Please try again.')
