import inflect

p = inflect.engine()

list = []
while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        print()
        break

print("Adieu, adieu, to " + p.join(list))