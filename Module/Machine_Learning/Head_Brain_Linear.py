import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousHeadBrainLinear(Datapath):
    Line = "-"*88
    df = pd.read_csv(Datapath)

    print("First few records of the dataset are : ")
    print(Line)
    print(df.head())
    print(Line)
    print(df.describe())
    print(Line)

    x = df[["Head Size(cm^3)"]]
    y = df[["Brain Weight(grams)"]]

    print("Independent variables are : Head Size")
    print("Dependent variables are :  Brain Weight")

    print("Total records in dataset are : ",x.shape) ## can also use __len__

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, test_size= 0.2, random_state=42)

    print("Dimension of Training Dataset : ",X_Train.shape)
    print("Dimension of Testing Dataset is : ",X_Test.shape)

    print(Line)

    model = LinearRegression()

    model.fit(X_Train, Y_Train)

    Y_Predict = model.predict(X_Test)

    msc = mean_squared_error(Y_Test, Y_Predict)
    rmse = np.sqrt(msc)
    r2 = r2_score(Y_Test, Y_Predict)

    print(Line)

    print("Mean Squared error is : ",msc)
    print("Root mean squared value is : ", rmse)
    print("R Square value is : ",r2)

    print(Line)




    

def main():
    MarvellousHeadBrainLinear("MarvellousHeadBrain.csv")


if __name__ == "__main__":
    main()