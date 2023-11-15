# create list of months
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# prompt user in a loop
while True:
    date = input("Date: ")
    # first format of dates
    try:
        m, d, y = date.split("/")
        if (0 < int(m) < 13) and (int(d) < 32):
            break
    except:
        # second format of dates
        try:
            m, d, y, = date.title().split(" ")
            # find the number of the month
            for i in range(len(month)):
                if m == month[i]:
                    m = i + 1
                    break
            # remove comma from day variable
            d = d.replace(",", "")
            # check if month and day is in between true values
            if (0 < int(m) < 13) and (int(d) < 32):
                break
        except:
            pass

print(f"{y}-{int(m):02}-{int(d):02}")