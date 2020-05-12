
# Functions bring ...
#     Reusability
#     Readability
#     Maintainability

truth = True

# if truth:
#     def add(n1, n2):
#         total = n1 + n2
#         return (total, n1, n2)
# else:
#     def add(n1, n2):
#         total = n1 + n2 + 1
#         return total



def add(n1, n2, *n3, absolute=False, **kwargs):
    '''add function add a collection of number together

    parameters:
        n1: first number (required)
        n2: second number (required) 
        n3: any other numbers (optional)
        absolute: named parameter. should we abs the result'''
    
    for key, value in kwargs.items():
        print(key, value)



    total = n1 + n2
    for n in n3:
        total += n

    if absolute:
        total = abs(total)

    return total


answer = add(21, 11, 10, -110, absolute=True,  width=100, height=10, depth=30)



print("answer", answer)
