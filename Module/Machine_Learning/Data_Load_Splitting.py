import sklearn
import pandas as pd


def main():
    df = pd.read_csv("iris.csv")                     ## df == dataframe

    print("dataset loaded successfully. ")

    print("dimension of dataset is : ",df.shape)

    #print(df["variety"])
    #print(df["sepal.length"].head)

    df["variety"] = df["variety"].map({"Setosa" : 0, "Versicolor" : 1, "Virginica" : 2})

    print(df["variety"])

    X = df.drop("variety", axis = "columns")            #axis ne horizontal or vertical cut kasa honare te kalta
    Y = df["variety"]
    print("independent variable dimension : ",X.shape)
    print("dependent variable dimension : ",Y.shape)

   

if __name__ == "__main__":
    main()  