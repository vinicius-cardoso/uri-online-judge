NAME = str(input())
FIXED_SALARY = float(input())
SALES = float(input())

TOTAL = FIXED_SALARY + 0.15 * SALES

print("TOTAL = R$ {0:.2f}".format(TOTAL))