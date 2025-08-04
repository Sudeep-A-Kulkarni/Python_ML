import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

def main():
    df = pd.read_csv("iris.csv")

    sns.pairplot(df, hue = "variety")

    plt.show()





if __name__ == "__main__":
    main()