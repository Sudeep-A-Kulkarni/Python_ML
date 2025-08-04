from sklearn import tree

#rough 0
#smooth 1

def main():
    Ball_Features = [[35, 0], [47, 0], [90, 1], [48, 0], [90, 1], [35,0], [92, 1], [35, 0], [35, 0], [35, 0]]

    Ball_Names = ["Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Tennis", "Tennis"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Ball_Features, Ball_Names)

    print(obj.predict([93, 1]))


if __name__ == "__main__":
    main()