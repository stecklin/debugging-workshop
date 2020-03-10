import random

from sklearn.datasets import fetch_openml


def exercise2():
    # --- PLAYGROUND EXAMPLE ---

    random_list = create_list(length=100, min_value=-5, max_value=100)
    # You wonder what happens if we call is_even() for negative numbers...
    # TODO: Set a conditional breakpoint in the loop (line 13), to only stop when the number is negative
    for number in random_list:
        if is_even(number):
            print("Number is even!")
        else:
            print("Number is odd!")
    print("You're done with the playground example!")

    # --- REAL CODE ---

    # Load data
    X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    # The following code applies the function split_home_destination() to every element in the column "home.dest"
    # TODO: Set a breakpoint into split_home_destination() below and check for the first elements how the function works
    # TODO: Make the breakpoint conditional and figure out for which kind of elements the function
    #  split_home_destination() throws an exception
    try:
        # Split column "home.dest" into city and state
        X["home.dest_city"], X["home.dest_state"] = X.apply(lambda row: split_home_destination(row["home.dest"]),
                                                            axis=1, result_type="expand")
    except Exception as e:
        print(e)
    print("You're done with exercise 2!")


def create_list(length=5, min_value=0, max_value=100):
    l = []
    for i in range(length):
        l.append(random.randint(min_value, max_value))
    return l


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def split_home_destination(destination):
    if not destination:
        return None, None
    destination_split = destination.rsplit(", ", 1)
    destination_city = destination_split[0]
    destination_state = destination_split[1]
    return destination_city, destination_state
