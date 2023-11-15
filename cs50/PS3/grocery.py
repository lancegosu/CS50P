item_list = {}
while True:
    try:
        item = input()
        if item in item_list:
            item_list[item] += 1
        else:
            item_list[item] = 1
    except EOFError:
        for item in sorted(item_list.keys()):
            print(f"{item_list[item]} {item.upper()}")
        break