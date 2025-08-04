import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report
def main():

    df = pd.read_csv("diabetes.csv")

    X = df.drop(columns= ["Outcome"])
    
    Y = df["Outcome"]

    scaler = StandardScaler()
    X_Scale = scaler.fit_transform(X)


    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X_Scale, Y, test_size=0.2, random_state=42)

    Log_CLF = LogisticRegression()

    DT_CLF = DecisionTreeClassifier(max_depth=8)

    KNN_CLF = KNeighborsClassifier(n_neighbors=7)


    voting_CLF = VotingClassifier(
        estimators= [
            ("lr", Log_CLF),
            ("dt", DT_CLF),
            ("knn", KNN_CLF)
        ],
        voting="hard"
    )
    voting_CLF.fit(X_Train, Y_Train)

    Y_Pred = voting_CLF.predict(X_Test)

    print("Accuracy score is : ")

    print(accuracy_score(Y_Test, Y_Pred)*100)



  
if __name__ == "__main__":
    main()