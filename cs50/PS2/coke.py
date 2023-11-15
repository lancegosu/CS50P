# amount = 50
# while amount > 0:
#     print("Amount Due:", amount)
#     pay = int(input("Insert Coin: "))
#     if pay != 5 and pay != 10 and pay != 25:
#         continue
#     amount -= pay

# print("Change Owed:", amount * -1)

amount = 50
while amount > 0:
    print("Amount Due:", amount)
    pay = int(input("Insert Coin: "))
    if pay == 5 or pay == 10 or pay == 25:
        amount -= pay

print("Change Owed:", amount * -1)