from sklearn import tree
from sklearn.datasets import fetch_openml


def exercise4():
    # --- PLAYGROUND EXAMPLE ---

    num_wishes = 3
    # TODO: Set a breakpoint in the following line, and change num_wishes to 5 before continuing
    print("Aladdin, I'm gonna grant you %d wishes!" % num_wishes)

    # --- REAL CODE ---

    # Load data
    X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    # Take a subset of columns and pre-process data
    X_subset = X[["age", "fare"]]
    X_subset = X_subset.fillna(X_subset.median())
    # Train a decision tree classifier on the data set
    classifier = tree.DecisionTreeClassifier()
    classifier = classifier.fit(X_subset, y)
    # TODO: Save X_subset to file (X_subset.to_csv("subset.csv"))
    print("You're done with exercise 4!")
