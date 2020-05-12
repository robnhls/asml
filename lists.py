
pets = ["Smokey", "Ferret", "Yoyo", "Rudolf" ]

print("Pet Count", len(pets))
print("All Pets", pets)

more_pets = list(pets) # list constructor

pets.extend(["Fido", "Yeller"])
print("-" * 30)
print("Pet Count", len(pets))
print("All Pets", pets)


# name = pets.pop()
# print("-" * 30)
# print("Pet Count", len(pets))
# print("All Pets", pets)


a_pet = pets[0]
last_pet = pets[-1] # -1 starts counting from the back of the list

#     0           1       2       3         4       5
# ['Smokey', 'Ferret', 'Yoyo', 'Rudolf', 'Fido', 'Yeller']
#    -6          -5       -4      -3        -2      -1


middle_pets = pets[1:5]
all_pets = pets  # 2 references (one list)
all_pets = pets[:] # shallow copy (two lists)

odd_pets = pets[1::2]

# not how python developer would write this
# last = len(pets)
# counter = 0
# while(counter < last):
#     print(pets[counter])
#     counter += 1


for pet_name in pets[::2]:
    print(pet_name)


# for index, name in enumerate(pets):


