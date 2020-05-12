
# data_file = open("data.txt", "r") # read in text mode

# colors = data_file.readlines()

# data_file.close()

# print(colors)


with open("data.txt", "r") as data_file:
    data = []

    for line in data_file: # readline until the end
        cleaned_line = line.strip()
        color, city = cleaned_line.split(",")

        data.append((city.title(), color))
        # or
        # colors.append(line[:-1])



print(data)