import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

        






def main():
    MarvellousAdvertise("Advertising.csv")
    
    
    
    
    
    
if __name__ == "__main__":

    main()