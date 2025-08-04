from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data

    target = iris.target

    X_Train, X_Test, Y_Train , Y_Test = train_test_split(data, target, test_size=0.5)

    model = tree.DecisionTreeClassifier()
    model.fit(X_Train, Y_Train)

    Predictions = model.predict(X_Test)

    Accuracy = accuracy_score(Predictions, Y_Test)

    return Accuracy

    

def main():
    result = MarvellousCalculateAccuracyDecisionTree()

    print("Accuracy of Decision Tree Classifier is: ", result*100)




if __name__ == "__main__":
    main()