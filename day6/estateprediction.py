#multiple-linear reg
import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([
    [2,60],
    [3,70],
    [4,75],
    [5,85],
    [6,90]
])
y=np.array([45,55,65,78,88])
model=LinearRegression()
model.fit(x,y)
print("coefficient",model.coef_)
print("intercept:",model.intercept_)
pred=model.predict([[7,95]])
print(pred)