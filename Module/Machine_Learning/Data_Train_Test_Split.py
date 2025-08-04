import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("iris.csv")                     

    print("dataset loaded successfully. ")


    df["variety"] = df["variety"].map({"Setosa" : 0, "Versicolor" : 1, "Virginica" : 2})

    X = df.drop("variety", axis = "columns")            
    Y = df["variety"]

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.2)

    print("dimension of X_Train : ",X_Train.shape)
    print("dimension of X_Test : ",X_Test.shape)
    print("dimension of Y_Train : ",Y_Train.shape)
    print("dimension of Y_Test : ",Y_Test.shape)    
    

   

if __name__ == "__main__":
    main()  