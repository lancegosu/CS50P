def main():
    time = input("What time is it? ")
    x = convert(time)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    if " " in minutes:
        minutes, ampm = minutes.split(" ")
 #      print(hours, minutes, ampm)
 #  if hours == 12:
 #  hours = 0
        hours = float(hours) % 12
        if "p.m." in ampm:
            hours += 12
    m = float(hours) + float(minutes) / 60.0
 #  print(m)
    return m


if __name__ == "__main__":
    main()