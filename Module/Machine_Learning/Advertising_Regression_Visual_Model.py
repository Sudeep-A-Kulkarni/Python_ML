import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import metrics

def MarvellousAdvertise(Dataset):

    Line = "-"*88

    df = pd.read_csv(Dataset)                           ##used to print csv

    print(Line)
    
    print("The top few elements are : ")
    print(df.head())                       ##prints the first few data

    print("Clean the data set : ")

    df.drop(columns=["Unnamed: 0"], inplace= True)

    print(Line)
    print("the updated data is : ")

    print(df.head())

    print(Line)

    print("Missing values in each collumn : ", df.isnull().sum())

    print(Line)

    print("The statistical data summary is : ")
    print(df.describe())
    print(Line)

    print("Co-relation matrix is :")

    print(df.corr())

    print(Line)


    plt.figure(figsize= (10,5))

    sns.heatmap(df.corr(), annot= True, cmap = "coolwarm")

    plt.title("Marvellous correlation visulation ")


    plt.show()

    sns.pairplot(df)

    plt.suptitle("Pairplot of features : ", y = 1.02)

    plt.show()

    x = df[["TV", "radio", "newspaper"]]
    y = df[["sales"]]


    X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, test_size= 0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_Train, Y_Train)
    
    Y_Pred = model.predict(X_Test)

    MSE = metrics.mean_squared_error(Y_Test,Y_Pred)
    RMSe = np.sqrt(MSE)
    r2 = metrics.r2_score(Y_Test,Y_Pred)

    print("MSe : ",MSE)
    print("RMSE : ",RMSe)
    print("R sq : ",r2)

    print(Line)
        
    print("model coefficent are:")
    for col, coef in zip(x.columns, model.coef_):
        print(f"{col} :{coef} ")

    print("intercept is : ", model.intercept_)
    print(Line)


    plt.figure(figsize=(10,5))

    plt.scatter(Y_Test, Y_Pred, color = "blue")
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales ")

    plt.title("Marvellous Advertisement")
    plt.grid(True)

    plt.show()






def main():
    MarvellousAdvertise("Advertising.csv")
    
    
    
    
    
    
if __name__ == "__main__":

    main()