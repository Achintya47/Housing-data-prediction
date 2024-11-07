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


mymodel1=numpy.poly1d(numpy.polyfit(x,y,3))#Polyfit for Polynomial regression

mymodel2=numpy.poly1d(numpy.polyfit(x,y,1))#Polyfit for Linear Regression

slope, intercept, r, p, std_err = stats.linregress(x, y) 
#Linear regression again, but this time using linregress method 

def myfunc(x):
    return slope*x + intercept

mymodel3=list(map(myfunc,x))

myline=numpy.linspace(2000,16000,100)

print("R2 score of Polynomial regression(degree 3): ",r2_score(y,mymodel1(x)))

print("R2 Score of Linear regression:",r2_score(y,mymodel3))

area1=int(input("Enter the area for Price prediction: "))

polyprice=mymodel1(area1)
print("The price using Polynomial Regression: ",polyprice)
linearprice=myfunc(area1)
print("The price using Linear Regression: ",linearprice)

plt.scatter(x,y,s=1.5)

plt.plot(myline,mymodel1(myline),label="PolynmialRegression (degree 3)")

plt.plot(myline + 100,mymodel2(myline),label="Linear Regression(Polyfit)")

plt.plot(x,mymodel3,label="Linear Regression(Linregress)")

plt.title("NostraPredict")

plt.xlabel("Area of houses")

plt.ylabel("Price of Houses")

plt.legend()

plt.show()
