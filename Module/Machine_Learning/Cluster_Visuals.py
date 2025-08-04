import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def main():

    dataset = pd.read_csv("iris.csv")

    X = dataset.iloc[:, [0, 1, 2, 3]].values

    print(X)
    
    WCSS = []

    for k in range(1, 11):
        model = KMeans(n_clusters=k, init= "k-means++", n_init= 10, random_state=42)
        model.fit(X)
        print(model.inertia_)
        WCSS.append(model.inertia_)

    plt.plot(range(1, 11), WCSS, marker = "o")
    plt.title("Ekbow method for KMEans")
    plt.xlabel("Value of K ")
    plt.ylabel("WCSS")
    plt.grid(True)
    plt.show()


    model = KMeans(n_clusters=3, init= "k-means++", n_init= 10, random_state=42)

    Y_KMeans = model.fit_predict(X)


    plt.scatter(X[Y_KMeans == 0 , 0], X[Y_KMeans == 0, 1], s = 100, c="red", label = "Setosa")

    plt.scatter(X[Y_KMeans == 1 , 0], X[Y_KMeans == 1, 1], s = 100, c="blue", label = "Versicolor")

    plt.scatter(X[Y_KMeans == 2 , 0], X[Y_KMeans == 2, 1], s = 100, c="green", label = "Virginica")

    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:,1], s = 100, c = "yellow", label = "Centroid")

    plt.legend()

    plt.show()




if __name__ == "__main__":
    main()