

# ValueError (no,five,number,100.4, 1,000)
# ZeroDivisionError

try:
    # open a file/db
    number = input ("Enter a whole number: ")
    number = int(number)

    # bail is a number is greater than 100
    if number > 100:
        raise Exception("we don't like numbers greater than 100")


    base_number = 100
    answer = base_number / number
    
except ValueError as err:
    print("'{}' is not a valid whole number".format(number))
    number = 50
except ZeroDivisionError as err:
    print("Cannot divide by zero. Probably should have mentioned that")
except Exception as err:
    print("Something bad happened")
    print("Type", type(err))
    print(err)
else:
    print("You are a rock star!")
    print("Your answer is {}.".format(answer))
finally:
    pass




print("Application has ended")
