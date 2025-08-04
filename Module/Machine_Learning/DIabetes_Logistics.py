import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def main():

    diabetes = pd.read_csv("diabetes.csv")

    print(diabetes.columns)

    print(diabetes.head())

    print(diabetes.shape)

    X = diabetes.drop(columns= ["Outcome"])
    
    Y = diabetes["Outcome"]

    print("The shape of X is : ")
    print(X.shape)
    print("The shape of Y is : ")
    print(Y.shape)


    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state=42)

    logreg = LogisticRegression().fit(X_Train, Y_Train)

    print("Training Accuracy is : ")
    print(logreg.score(X_Train, Y_Train))

    print("Testing Accuracy is : ")
    print(logreg.score(X_Test, Y_Test))

    


 


if __name__ == "__main__":
    main()