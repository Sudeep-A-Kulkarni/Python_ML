import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def main():
    df = pd.read_csv('iris.csv')

    sns.boxplot(x="variety", y="petal.length", data = df)
    plt.title("Marvellous Box Plot for Petal Length by Variety")

    plt.show()


if __name__ =="__main__":
    main()