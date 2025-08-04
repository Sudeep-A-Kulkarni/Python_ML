from sklearn import tree

def main():
    Ball_Features = [[35, "Rough"], [47, "Rough"], [90, "Smooth"], [48, "Rough"], [90, "Smooth"], [35,"Rough"], [92, "Smooth"], [35, "Rough"], [35, "Rough"], [35, "Rough"]]

    Ball_Names = ["Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Tennis", "Tennis"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Ball_Features, Ball_Names)

    print(obj.predict([93, "Smooth"]))


if __name__ == "__main__":
    main()