# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import accuracy_score, mean_absolute_error,r2_score
# import joblib
#
# df=pd.read_csv("D:/final2 jee.csv")
#
# X=df[["Marks"]]
# y=df["Percentile"]
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#
# model =RandomForestRegressor(n_estimators=200,random_state=42)
#
# model.fit(X_train,y_train)
#
# prediction=model.predict(X_test)
# mae=mean_absolute_error(y_test,prediction)
# r2=r2_score(y_test,prediction)
#
# joblib.dump(model,"model1_marks_to_percentile.pkl")
# loaded_model = joblib.load("model1_marks_to_percentile.pkl")
# marks = float(input("Enter your JEE Marks: "))
# predicted_percentile = loaded_model.predict([[marks, year]])
#
# from sklearn.model_selection import cross_val_score
# scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')

# train_model1.py

import joblib
import numpy as np

# Load trained model
model = joblib.load("model1_marks_to_percentile.pkl")

def prediction(marks: float):
    if not (0 <= marks <= 300):
        raise ValueError("Marks must be between 0 and 300.")

    result = model.predict(np.array([[marks]]))
    return float(result[0])

