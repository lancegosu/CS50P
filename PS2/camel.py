name = input("camelCase: ")
print("snake_case: ", end="")
for i in range(len(name)):
    if name[i].isupper():
        print("_" + name[i].lower(), end="")
    else:
        print(name[i], end="")

print()