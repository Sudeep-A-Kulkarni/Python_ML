import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score



def main():
    df = pd.read_csv("Telco-Customer-Churn.csv")

    print(df.shape)

    df.drop(["customerID", "gender"],axis = 1, inplace = True)

    for col in df.select_dtypes(include="object"):
        df[col] = LabelEncoder().fit_transform(df[col])

    #print(df.head)

    X = df.drop("Churn", axis=1) ##doubt
    Y = df["Churn"]

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, random_state=42, test_size=0.2)

    model = RandomForestClassifier(n_estimators=150, max_depth=7, random_state= 42)

    model.fit(X_Train, Y_Train)

    Y_Pred = model.predict(X_Test)

    print("Accuracy is: ",accuracy_score(Y_Test, Y_Pred)*100)















    

if __name__ == "__main__":
    main()