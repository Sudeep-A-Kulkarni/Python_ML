#import pandas as pd
import math
import numpy as np
#import matplotlib.pyplot as plt
#import sklearn
#     A, B, C, D
# X = 1, 2, 3, 6
# Y = 2, 3, 1, 5
def Euc_Distane(P1, P2):
    Ans = math.sqrt((P1["x"]-P2["x"])**2 + (P1["y"]-P2["y"])**2)
    return Ans


def Marvellous_KNN():
    line = "-"*100
    data = [{"point" : "A", "x" : 1, "y" : 2, "label" : "Red"},
            {"point" : "B", "x" : 2, "y" : 3, "label" : "Red"}, 
            {"point" : "C", "x" : 3, "y" : 1, "label" : "Blue"}, 
            {"point" : "D", "x" : 6, "y" : 5, "label" : "Blue"}]
    print(line)
    print("training data set : ")
    print(line)


    for i in data:
        print(i)

    print(line)

    new_point = {"x" : 3,"y" : 3}
    for d in data:
        d["distance"] = Euc_Distane(d, new_point)

    print(line)

    print("calculated distances are : ")

    for d in data:
        print(d)

    print(line)

    sorted_data = sorted(data, key = lambda item : item["distance"])

    print("sorted data is : ")
    for d in sorted_data:
        print(d)

    print(line)

    k = 3

    nearest = sorted_data[:k]

    print(line)
    print("sorted 3 elements are")
    for d in nearest:
        print(d)

    print(line)

    votes = {}


    for neighbour in nearest:
        label = neighbour["label"]
        votes[label] = votes.get(label,0) + 1
     
    print(line)

    print("Result of voting is : ")
    for d in votes:
        print("Name : ",d,"Value : ",votes[d])

    print(line)

    predicted_class = max(votes, key = votes.get)

    print("Predicted class for the point (3,3) is : ",predicted_class)

def main():
    print("Demonstration of KNN algorithm. ")
    Marvellous_KNN()
    


if __name__ == "__main__":
    main()