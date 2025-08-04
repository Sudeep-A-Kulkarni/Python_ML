import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def main():

    dataset = pd.read_csv("iris.csv")

    X = dataset.iloc[:, [0, 1, 2, 3]].values

    print(X.shape)


    model = KMeans(n_clusters=3, init= "k-means++", n_init= 10, random_state=42)

    Y_KMeans = model.fit_predict(X)

    print("The value of Y_KMeans : ")

    print(Y_KMeans.shape)

    print("CLuster of Setosa : 0")

    for i in range(0,10):
        print(X[i], Y_KMeans[i])

    print("CLuster of Versicolor : 1")

    for i in range(51, 61):
        print(X[i], Y_KMeans[i])


    print("CLuster of Virginica : 2")

    for i in range(101, 111):
        print(X[i], Y_KMeans[i])
    


if __name__ == "__main__":
    main()