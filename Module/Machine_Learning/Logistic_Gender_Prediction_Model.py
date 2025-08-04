import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



def Marvellous_Logistics(datasetpath):
    df = pd.read_csv(datasetpath)

    print("Dimension of the data shape is : ",df.shape)             #Gives the shape of the data

    print("Initial data is : ",df.head(5))                          #gives top 5 data 

    df["Gender"] = df["Gender"].map({"Female" : 0, "Male" : 1})     #when () / []


    print("Encoded data is : ")
    print(df.head())

    plt.figure(figsize=(8, 6))
    sns.scatterplot(df, x = "Height", y = "Weight", hue= "Gender", palette="Set1" )
    plt.title("Marvellous height weight gender predictor. ")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()

    X = df[["Height", "Weight"]]
    Y = df[["Gender"]]

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state= 42)

    model = LogisticRegression()

    model.fit(X_Train, Y_Train)

    Y_Predict = model.predict(X_Test)

    Accuracy_Score = accuracy_score(Y_Test, Y_Predict)

    print("The accuracy is : ",Accuracy_Score*100)

    Confusion_Matrix = confusion_matrix(Y_Test, Y_Predict)

    print("The confusion matrix is : ")
    print(Confusion_Matrix)

    report = classification_report(Y_Test, Y_Predict)

    print("the clasification report is  : ")
    print(report)








def main():
    Marvellous_Logistics("weight-height.csv")

if __name__ == "__main__":
    main()