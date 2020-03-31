X, Y = map(int, input().split())

if (X == 1):
    price = 4.00
elif (X == 2):
    price = 4.50
elif (X == 3):
    price = 5.00
elif (X == 4):
    price = 2.00
elif (X == 5):
    price = 1.50
else:
    print("Valor invalido")

total = price * Y

print("Total: R$ {0:.2f}".format(total))