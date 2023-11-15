while True:
    fraction = input("Fraction: ")

    try:
        x, y = fraction.split("/")
#       print(x, y)
        x = int(x)
        y = int(y)
        percentage = (x / y) * 100
        percentage = round(percentage)
        if percentage <= 1:
            print("E")
        elif x > y:
            continue
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break
    except ValueError:
#       print("Wrong")
        pass
    except ZeroDivisionError:
#       print("No")
        pass