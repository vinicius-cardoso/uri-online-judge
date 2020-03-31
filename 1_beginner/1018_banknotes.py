import math

value1 = int(input())

one_hundred = math.floor(float(value1 / 100))
value2 = value1 - one_hundred * 100

fifty = math.floor(float(value2 / 50))
value3 = value2 - fifty * 50

twenty = math.floor(float(value3 / 20))
value4 = value3 - twenty * 20

ten = math.floor(float(value4 / 10))
value5 = value4 - ten * 10

five = math.floor(float(value5 / 5))
value6 = value5 - five * 5

two = math.floor(float(value6 / 2))
value7 = value6 - two * 2

one = math.floor(float(value7 / 1))
value8 = value7 - one * 1

print(value1)
print("{0:.0f} nota(s) de R$ 100,00".format(one_hundred))
print("{0:.0f} nota(s) de R$ 50,00".format(fifty))
print("{0:.0f} nota(s) de R$ 20,00".format(twenty))
print("{0:.0f} nota(s) de R$ 10,00".format(ten))
print("{0:.0f} nota(s) de R$ 5,00".format(five))
print("{0:.0f} nota(s) de R$ 2,00".format(two))
print("{0:.0f} nota(s) de R$ 1,00".format(one))