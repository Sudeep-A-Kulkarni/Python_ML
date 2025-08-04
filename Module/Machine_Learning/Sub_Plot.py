import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

def main():
    iris = load_iris()
    X = iris.data
    Y = iris.target

    fig = plt.figure(figsize= (8, 6))

    ax = fig.add_subplot(111, projection = "3d")
    ax.scatter(X[:,2], X[:,3], X[:,0], c = Y, cmap = "viridis", edgecolors="k")

    ax.set_xlabel("Petal Length")
    ax.set_ylabel("Petal Width")
    ax.set_zlabel("Sepal Length")

    plt.title("Marvellous 3D visualisation for iris ")


    plt.show()





if __name__ == "__main__":
    main()