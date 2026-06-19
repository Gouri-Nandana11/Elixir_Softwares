import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([20,45,80,130,200])
poly=PolynomialFeatures(degree=2)
x_train=poly.fit_transform(x)
model=LinearRegression()
model.fit(x_train,y)
pred=model.predict(poly.transform([[6]]))
print(pred)