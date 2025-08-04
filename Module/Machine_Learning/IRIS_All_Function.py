import pandas as pd
from sklearn.model_selection import train_test_split


def LoadData(file_path):
    df = pd.read_csv(file_path)
    print("data set gets loaded in memory successfully. ")
    return df

def GetInformation(df):
    print("information about the loaded dataset is : ")
    print("shape of data set is: ",df.shape)

    print("collumns : ",df.columns)
    print("Missing values : ",df.isnull().sum())


def EncodeData(df):
    df["variety"] = df["variety"].map({"Setosa":0, "Versicolor":1, "Virginica":2})


def split_featue_target(df):
    X = df.drop("variety", axis = 1)
    Y = df("variety")
   

    print(X)
    return X, Y

#def Split(X, Y, size):
 #   return train_test_split(X, Y, test_size=size)


def main():
    data = LoadData("iris.csv")

    print(data.head())

    GetInformation(data)

    print("data after encoding")
    EncodeData(data)

    print(data.head())

    print("Splitting Features and labels are")
    Independent, Dependent = split_featue_target(data)
    print(Independent.head())
    print(Dependent.head())

    X_Train,X_Test,Y_Train,Y_Test = train_test_split[(Independent,Dependent,0.3)]
    print(X_Train.shape)
    print(X_Test.shape)
    print(Y_Train.shape)
    print(Y_Test.shape)




if __name__ == "__main__":
    main()