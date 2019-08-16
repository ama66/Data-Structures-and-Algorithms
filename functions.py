# * tells Python to accept an unlimited amount of unnamed arguments and pass them into the function as a tuple
# ** tells Python to accept and unlimited amount of named arguments and pass them into the function as a dictionary
def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)


unlimited_arguments(1,2,3,4, name='Max', age=29) 