def my_decorator(func):
    def wrapper():
        print('+---------+')
        print('|         |')
        result = func()
        print(result)
        print('|         |')
        print('+=========+')
        return result
    return wrapper
 
@my_decorator
def print_fibonacci():
    '''Print out Fibonacci'''
    return ' Fibonacci '

print_fibonacci()