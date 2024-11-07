import matplotlib.pyplot as plt
import numpy
import csv
from scipy import stats
from sklearn.metrics import r2_score

x=[]
y=[]
with open("Housing.csv") as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        x.append(int(row['area']))
        y.append(int(row['price']))

mymodel=numpy.poly1d(numpy.polyfit(x,y,2))
mymodel2=numpy.poly1d(numpy.polyfit(x,y,1))

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope*x + intercept

mymodel3=list(map(myfunc,x))
myline=numpy.linspace(2000,16000,100)

print(r2_score(y,mymodel(x)))
print(r2_score(y,mymodel2(x)))
print(r2_score(y,mymodel3))


plt.scatter(x,y,s=1.5)

plt.plot(myline,mymodel(myline),label="Polynmial degree=3")

plt.plot(myline + 100,mymodel2(myline),label="Linear")

plt.plot(x,mymodel3,label="Linregress function")

plt.title("Supervised Learning:Regression")

plt.xlabel("Area")

plt.ylabel("Price of Houses")

plt.legend()

plt.show()
