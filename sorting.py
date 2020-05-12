

def make_lower(pie):
    print("** Debug ***", pie)
    return len(pie), pie.lower()


pies = ["peach", "apple", "pumpkin", "Lemon", "blueberry"]

sorted_pies = sorted(pies, key=make_lower, reverse=True)

print(sorted_pies)