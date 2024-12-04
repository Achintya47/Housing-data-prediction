import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("Housing.csv")

X=df[['area','bedrooms','bathrooms','stories','parking']]
Y=df[["price","area"]]

corr1= X.corr()
corr2=Y.corr()
print(corr1)
print(corr2)

sns.heatmap(corr1,cmap="RdBu")


plt.show()
