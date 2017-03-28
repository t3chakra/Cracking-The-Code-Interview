def mydecorator(some_function):
    def wrapper():
        print "hello"
        some_function()
        print "bye"
    return wrapper
def just_a_function():
    print "inside the decorator"

a=mydecorator(just_a_function)
a()

@mydecorator
def just_a_second_function():
    print "love u lutuputu"

just_a_second_function()