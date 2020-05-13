import csv

data = [
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
    ("rob", "foulkrod","monroe, mi"),
]

with open("people.csv", "w") as out_file:
    people_writer = csv.writer(out_file)
    for person in data:
        people_writer.writerow(person)

print("all done")


