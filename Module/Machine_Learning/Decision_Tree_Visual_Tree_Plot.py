from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 
from sklearn.tree import plot_tree

def MarvellousDecisionTree():
    iris = load_iris()
    
    X = iris.data
    Y = iris.target

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.2)

    model = DecisionTreeClassifier()

    model.fit(X_Train, Y_Train)

    Y_Predict =  model.predict(X_Test)

    accuracy = (accuracy_score(Y_Test, Y_Predict))

    print("the accuracy of the model is : ", accuracy * 100)

    plt.figure(figsize=(12, 8))
    plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
    plt.title("Marvellous Decision Tree CLassifier . ")
    plt.show()


def main():
    MarvellousDecisionTree()
    
if __name__ =="__main__":
    main()