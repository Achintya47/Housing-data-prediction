import csv
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


x=[]
y=[]
with open('Housing.csv') as file:
    csv_file=csv.DictReader(file)
    for row in csv_file:
        x.append(int(row['area']))
        y.append(int(row['price']))

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope*x + intercept

print(myfunc(3120))

regressmodel=list(map(myfunc,x))


plt.scatter(x,y,s=1.5)
plt.plot(x,regressmodel)
plt.show()