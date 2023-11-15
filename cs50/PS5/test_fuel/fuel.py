def main():
    str = input("Fraction: ")
    str = convert(str)
    str = gauge(str)
    print(str)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    percentage = (x / y) * 100
    if x > y:
        raise ValueError
    percentage = round(percentage)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()