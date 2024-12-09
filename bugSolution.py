def my_function(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 0