from sklearn import tree

#rough 0
#smooth 1

def main():
    Ball_Features = [[35, 0], [47, 0], [90, 1], [48, 0], [90, 1], [35,0], [92, 1], [35, 0], [35, 0], [35, 0]]
#   tennis = 1
#   cricket = 2
    Ball_Names =[ 1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Ball_Features, Ball_Names)

    print(obj.predict([[93, 1]]))
    



if __name__ == "__main__":
    main()