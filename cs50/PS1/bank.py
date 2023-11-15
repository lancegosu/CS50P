a = input("Greeting: ")
if a.lower().strip().startswith("hello"):
    print("$0")
elif a.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")