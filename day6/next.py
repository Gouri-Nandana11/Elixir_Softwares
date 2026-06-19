import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
x=np.array([
    [1,60],
    [2,65],
    [3,70],
    [4,75],
    [5,80],
    [6,90]
    ])
y=np.array([25,30,38,45,55,68])
model=LinearRegression()
model.fit(x,y)
y_pred=model.predict(x)
print("coeficient:",model.coef_)
print("intercept",model.intercept_)
print("best fit :",model.coef_[0],"x+",model.coef_[1],"x2+",model.intercept_)
pred=model.predict([[2500,5]])
print("predicted value:",pred)
print("mse",mean_absolute_error(y,y_pred))
print(r2_score,r2_score(y,y_pred))