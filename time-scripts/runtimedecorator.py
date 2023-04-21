import time

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print (f.__name__, 'took', end - start, 'time')
        return result
    return f_timer # @timefunc for time measurments

# - - - - - - - - -
# example 
@timefunc # func
def example():
    for i in range(100):
        print('This does something')
    return

example()
