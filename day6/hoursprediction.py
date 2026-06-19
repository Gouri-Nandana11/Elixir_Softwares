import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
x=np.array([1000,1200,1500,1800,2000]).reshape(-1,1)
y=np.array([30,36,45,54,60])
model=LinearRegression()
model.fit(x,y)
y_pred=model.predict(x)
print("slope:",model.coef_[0])
print("intercept:",model.intercept_)
pred=model.predict([[2200]])
print(pred)
print("MAE",mean_absolute_error(y,y_pred))
print("MSE",mean_squared_error(y,y_pred))
print("RMSE",mean_squared_error(y,y_pred)**0.5)
print("R2:",r2_score(y,y_pred))