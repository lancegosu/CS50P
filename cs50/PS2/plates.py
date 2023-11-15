def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
#   check if size in the range is 2 to 6
    if len(s) < 2 or len(s) > 6:
        return False

#   check if plate starts with two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

#   check if numbers not followed by letters
    met_number = False
    for i in range(len(s)):
        if s[i].isdigit():
#           check if first digit is 0, then plate is invalid
            if s[i] == "0" and met_number == False:
                return False
            met_number = True
        elif s[i].isalpha():
            if met_number == True:
                return False
        else:
            return False

    return True



main()