#minitask 7

def deprecated(func):
    def inner(*args):
        print('Call to deprecated function: {}'.format(func.__name__))
        val = func(*args)
        print('{}'.format(val))
        return val
    return inner

@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,2)

# should write:
# Call to deprecated function: some_old_function
# 3 