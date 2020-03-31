CODE1, UNITS1, PRICE1 = input().split()
CODE2, UNITS2, PRICE2 = input().split()

VALOR = int(UNITS1) * float(PRICE1) + int(UNITS2) * float(PRICE2)

print("VALOR A PAGAR: R$ {0:.2f}".format(VALOR))