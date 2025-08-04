import pandas as pd

def main():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

    header = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

    dataframe = pd.read_csv(url, names = header)

    print(dataframe)

if __name__ == "__main__":
    main()