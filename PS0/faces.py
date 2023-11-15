def main():
    x = input("How do you feel? ")
    y = convert(x)
    print(y)


def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")


main()