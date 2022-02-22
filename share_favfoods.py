print("Healthy people share with us your favoite foods.")
print("hit enter after each entry, Q to quit.")

favs = []

while True:
    data = input()
    if str.lower(data) == "q":
        break
    favs.append(data)

for food in favs:
    print("You said:", food)