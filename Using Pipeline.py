import matplotlib.pyplot as plt
import numpy
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

df=pd.read_csv("/kaggle/input/housing-prices-data/Housing.csv")
X=df[["area","bedrooms","bathrooms","stories","parking"]]
y=df["price"]


# imputer=SimpleImputer(stratey='mean')

# imputer=imputer.fit(X)
# X=imputer.transform(X)

# scaler=StandardScaler()

# X=scaler.fit_transform(X)
# y-scaler.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipeline=Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

# pipeline=Pipeline([
#     ('imputer', SimpleImputer(strategy='mean')),
#     ('scaler', StandardScaler()),
#     ('model', RandomForestRegressor(n_estimators=100, random_state=42))
# ])


pipeline.fit(X_train,y_train)

predictions=pipeline.predict(X_test)

print(mean_absolute_percentage_error(predictions,y_test))    
