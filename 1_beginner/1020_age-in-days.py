import math

dias_total = int(input())

anos = math.floor(dias_total / 365)
resultado1 = dias_total - anos * 365

meses = math.floor(resultado1 / 30)
dias = resultado1 - meses * 30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))