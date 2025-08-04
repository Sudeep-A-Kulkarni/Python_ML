import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def Marvellous_Predictor():
    ##Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("values of independent variable : ",X)
    print("value of dependent variable : ",Y)

    mean_X = np.mean(X)

    mean_Y = np.mean(Y)

    print("Mean of X : ",mean_X)
    print("Mean of Y : ",mean_Y)

    n = len(X)

    numerator = 0
    denominator = 0
    
    # y = mx + c

    for i in range(n):
        numerator = numerator + (X[i] - mean_X) * (Y[i] - mean_Y)
        denominator = denominator + (X[i] - mean_X)**2


    m = numerator / denominator


    print("slope of line is :  ", m)

    c = mean_Y - (m * mean_X)

    print("y intercept of line is : ",c)

    x = np.linspace(1, 6, n)

    y = c + m * x

    plt.plot(x, y, color = "g", label = "Regression Line")

    plt.scatter(X, Y, color = "r", label = "Scatter plot")

    plt.xlabel("X : Independent Variable ")
    plt.ylabel("Y : Dependent Variable ")

    plt.legend()
    

    plt.show()



    


    
                        

def main():
    Marvellous_Predictor()


if __name__ == "__main__":
    main()