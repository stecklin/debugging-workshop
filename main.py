import argparse
from ex1_navigation import exercise1
from ex2_conditional_breakpoints import exercise2
from ex3_variables_and_watches import exercise3
from ex4_evaluate_expressions import exercise4

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exercise', type=int, default=0, help='Number of the current exercise')
    args = parser.parse_args()

    # TODO: Set a breakpoint in the following line
    if args.exercise == 0:
        print("You're done with exercise 0!")
    elif args.exercise == 1:
        exercise1()
    elif args.exercise == 2:
        exercise2()
    elif args.exercise == 3:
        exercise3()
    elif args.exercise == 4:
        exercise4()
