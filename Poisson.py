import math
import random
from decimal import Decimal

class Array: 
    def __init__(self, x,fmin,fmay):
        self.x = x
        self.fmin = fmin
        self.fmay =  fmay

    def __repr__(self):
        return '{:f} : {:f} : {:f}'.format(self.x, self.fmin, self.fmay)

main_array = []

dias = int(input("Ingrese la cantidad de días:\n"))
dias = round(dias)
if 0>=dias:
    while True:
        dias = int(input("Ingrese un valor válido:\n"))
        dias = round(dias)
        if 0<dias:
            break

count=0
#fmin = 1
fmay=0

while fmay <= 0.999 or count < 170:
        fmin = (math.exp(dias*-1) * (dias**count))/math.factorial(count)

        fmay = fmay+fmin

        
        main_array.append(Array(count, fmin, fmay))
        count += 1


total=0


for i in range(0, len(main_array)-1):
    if i>=dias:
        break
    num = random.uniform(0,1)

    for j in range(0, len(main_array)-1):
        if num>main_array[j].fmay and num<=main_array[j+1].fmay:

            total=total+main_array[j].x


print("XTotal = " + str(total) + "\n")