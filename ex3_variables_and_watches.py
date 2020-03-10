from collections import Counter

import pandas as pd

from ex1_navigation import function_to_step_into_level_1
from ex2_conditional_breakpoints import create_list


def exercise3():
    # --- VARIABLES ---

    # TODO: Step through the following lines and look at the "Variables" view
    text = 'This variable is a string!'
    number = 123
    random_dict = {
        'a': 1,
        'b': 'value for b',
        'c': 0.5,
        'd': True
    }
    random_list = create_list(length=20, min_value=1, max_value=10)
    ordered_list = list(range(20))

    # TODO: Find the data_frame variable and click "View as DataFrame"
    data_frame = pd.DataFrame({'random_order': random_list, 'in_order': ordered_list})

    # --- WATCHES ---

    # TODO: Add "len(counter)" and "counter.most_common(1)" to "Watches" view and step through the loop
    counter = Counter()
    for char in "Cookie":
        counter.update(char)

    # --- VARIABLE HIERARCHY ---

    # TODO: Repeat exercise 1 (step into the functions) and look at the variable hierarchy ("Frames" + "Variables" view)
    function_to_step_into_level_1()

    # TODO: Try the same for a recursive function (step deeper into it until n == 0 and look at the variable hierarchy)
    fac = factorial(5)

    print("You're done with exercise 3!")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
