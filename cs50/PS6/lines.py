import sys
import os

def count(filename):
    counter = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                counter += 1
    return counter

path = sys.argv[1]
print(path)
# counter = count(filename)

total = 0
for path, subdirs, files in os.walk(path):
    for filename in files:
        # print(os.path.join(path, name))

# path = "."
# dir_list = os.listdir(path)
# for filename in dir_list:
        if not filename.endswith(".py"):
            continue
        print(filename)
        counter = count(path + "/" + filename)
        print(f"{path + '/' + filename} contains {counter} lines of code.")
        total += counter

print(total)