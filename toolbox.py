
'''Demo Toolbox

It contains a collection of functions and classes to make your life easier.

(not really)'''

def print_line(characters):
    '''print_line will print an ascii line

    Parameters
       characters:  the number of characters in the line to print
    '''
    print("-" * characters)

print("*** DEBUG ***", "the Toolbox module has been loaded")


# some simple toolbox tests
# the _ in front of the main means "private" and not to be called by the outside world
def _main():

    print_line(10)
    print_line(20)
    print_line(30)
    # __name__ in interactive mode is __main__
    # __name__ in module mode is toolbox

    print("Mode", __name__)

if __name__ == "__main__":
    _main()