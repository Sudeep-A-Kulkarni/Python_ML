import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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



def main():
    Marvellous_Logistics("weight-height.csv")

if __name__ == "__main__":
    main()