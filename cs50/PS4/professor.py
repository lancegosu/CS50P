import random

def main():
    level = get_level()
    correct_ans = 0
    for i in range(3):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        tries = 3
        while True:
            if tries == 0:
                print(f"{x} + {y} = {ans}")
                break
            user_ans = input(f"{x} + {y} = ")
            if not user_ans.isnumeric() or int(user_ans) != ans:
                print("EEE")
                tries -= 1
                continue
            else:
                correct_ans += 1
                break
    print("Score:", correct_ans)



def get_level():
    while True:
        n = input("Level: ")
        if not n.isnumeric():
            continue
        n = int(n)
        if n < 1 or n > 3:
            continue
        else:
            return n


def generate_integer(level):
    # if level == 1:
    #     number = random.randint(0, 9)
    # elif level == 2:
    #     number = random.randint(10, 99)
    # elif level == 3:
    #     number = random.randint(100, 999)
    # return number

    return random.randint(10 ** (level - 1), (10 ** level) - 1)

if __name__ == "__main__":
    main()