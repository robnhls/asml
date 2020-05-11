
import sys # there is a built in Library named sys

# python read.py 12 "cool parameter"

print("sys.argv", sys.argv)
# sys.argv is a list
# [ ] usually means list
executed_path = sys.argv[0]

if len(sys.argv) > 1:
    p1 = sys.argv[1]
else:
    p1 = input("enter a number: ")


# print a number of stars
times = int(eval(p1)) # convert p1 into an int

print("*" * times)


