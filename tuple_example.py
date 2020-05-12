
person1 = ("rob", "foulkrod", 47, "detroit")
person2 = ("alice", "jones", 48, "dallas")
person3 = "bob", "andrews", 49, "cleveland" # still a tuple even without the ()

# person2 = ("new", "name", 24, "ht") #replacing a tuple

people = [person1, person2, person3] # list of tuples

for first_name, last_name, _, home_town in people:
    # version 1
    print(f"{first_name} {last_name} is from {home_town}.")
    # version 2
    print("{} {} is from {}.".format(first_name, last_name, home_town))
    



# once you create a tuple, it is frozen (immutable)
# tuples often reflect records, rows

# print(person1)

first_name = person1[0]
last_name = person1[1]
age = person1[2]
home_town = person1[3]


# unpack a tuple easily
last_name, garbage, home_town = person1[1:]



# Not often done in a tuple
# for attribute in person1:
#     print(attribute)
print("-" * 60)
# print out a numbered list of first names
for index, person in enumerate(people, 1):
    print(index, person[0])