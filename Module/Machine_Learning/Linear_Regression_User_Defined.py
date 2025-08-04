import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def Marvellous_Predictor():
    ##Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("values of independent variable : ",X)
    print("value of dependent variable : ",Y)

    mean_X = 0

    mean_Y = 0

    X_sum = 0
    Y_sum = 0

    for i in range(len(X)):

        X_sum = X_sum + X[i]
        Y_sum = Y_sum + Y[i]

    mean_X = X_sum / len(X)
    mean_Y = Y_sum / len(Y)

    print("Mean of X : ",mean_X)
    print("Mean of Y : ",mean_Y)


    
                            







def main():
    Marvellous_Predictor()


if __name__ == "__main__":
    main()