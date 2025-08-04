from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def main():
    y_actual = [10, 20, 30, 40, 50]
    y_predicted = [10, 20, 30, 40, 50]


    MSE = mean_squared_error(y_actual, y_predicted)

    RMSE = np.sqrt(MSE)
    print("Actual values are : ",y_actual)
    print("predicted values are : ", y_predicted)
    print("Mean Squared Error : ",MSE)
    print("Root Mean Square Error : ",RMSE)



if __name__ == "__main__":
    main()