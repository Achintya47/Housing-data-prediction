#Multiple regression
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score


df=pd.read_csv('Housing.csv')

X=df[['area','bedrooms','bathrooms','stories']] #Starting with two variables

Y=df['price']

regrobj=linear_model.LinearRegression()

regrobj.fit(X,Y)

predlist=[]
y1=[]

for index,row in df.iterrows():
    y1.append(row['price'])


for index, row in df.iterrows():
    x1=row['area']
    x2=row['bedrooms']
    x3=row['bathrooms']
    x4=row['stories']
    predlist.append((regrobj.predict([[x1,x2,x3,x4]])))

x1=int(input("Enter the Area: "))
x2=int(input("Enter the Bedrooms: "))
x3=int(input("Enter the Bathrooms: "))
x4=int(input("Enter the Stories: "))



predvalue=regrobj.predict([[x1,x2,x3,x4]])

print("Predicted House Price is: ",predvalue)

print("R2 Score for multiple regress: ",r2_score(y1,predlist))

print(regrobj.coef_)





