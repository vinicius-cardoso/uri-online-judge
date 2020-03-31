import math

N = int(input())

hours = math.floor(N / 3600)
hours1 = N - hours * 3600

minutes = math.floor(hours1 / 60)  
seconds = hours1 - minutes * 60

print("{}:{}:{}".format(hours, minutes, seconds))