from sklearn.datasets import load_iris
from sklearn import tree


def exercise1():
    # --- PLAYGROUND EXAMPLE ---

    # TODO: Set a breakpoint at line 15 (>>> function_to_step_into_level_1())
    # TODO: Resume program to skip the variable creation lines
    s = "Let's create some variables!"
    x = 1
    y = 2
    z = 3
    # TODO: Step into this function
    function_to_step_into_level_1()
    print("You're done with the playground example!")

    # --- REAL CODE ---

    # Load data
    X, y = load_iris(return_X_y=True)
    # Train a decision tree classifier on the data set
    classifier = tree.DecisionTreeClassifier()
    # TODO: Check out how fit() works practicing resume program, step over, step into and step out
    # e.g. step into check_classification_targets() (line 173)
    # e.g. set a breakpoint and resume to where the tree is build (line 322)
    classifier = classifier.fit(X, y)
    print("You're done with exercise 1!")


def function_to_step_into_level_1():
    text = "I'm a level 1 function!"
    # TODO: Step into this function
    function_to_step_into_level_2()


def function_to_step_into_level_2():
    text = "I'm a level 2 function!"
    # TODO: Step over this function
    function_to_step_over()
    # TODO: Step into this function
    function_to_step_into_and_step_out()


def function_to_step_over():
    text = "I'm a boring function, you should have stepped over me!"


def function_to_step_into_and_step_out():
    text = "Here comes the interesting part!"
    interesting_var = 2
    for i in range(interesting_var):
        print("Interesting!")
    # TODO: Step out of this function
    text = "Now comes the boring part!"
    boring_var = "Why are you still here? You should have stepped out already!"
    more_boring_var = text + " " + boring_var
