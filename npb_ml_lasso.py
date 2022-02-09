from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

hr_features = pd.read_csv("npb_ht.csv")
hr_target = pd.read_csv("npb_htr.csv")

x_train, x_test, y_train, y_test = train_test_split(hr_features, hr_target, test_size =0.25, random_state=0)

Lasso = Lasso(alpha=0.1, random_state=0)
Lasso.fit(x_train, y_train)

n = int(input("選手番号:"))
print(y_test.index.to_list())
target_Lasso = Lasso.predict(x_test)
print(np.round(target_Lasso))
print(hr_target.iloc[[n], [0]])
print(Lasso.predict(hr_features.iloc[[n], [n for n in range(0, 16)]]))