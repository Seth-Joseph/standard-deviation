import math
import csv

with open('data.csv',newline = '')as f :
    reader = csv.reader(f)
    data = list(reader)
d = data.pop(0)
                                #Finding Mean
def mean(d):
    n = len(d)
    total = 0
    for i in d :
        total = total+int(i)
    mean = total/n
    return mean
   

                                #Squaring and getting values
square_list = []
for num in d:
    a = int(num)-mean(d)
    a = a**2
    square_list.append(a)
                                #Getting the sum
sum = 0
for i in square_list:
    sum = sum + i

result = sum/(len(d)-1)
STDEV = math.sqrt(result)
print(float(STDEV))
