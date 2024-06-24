x = input("Greeting: ")
x = x.lower().strip()
if (x.startswith("h") and x.startswith("hello") == False):
    print("$20")
elif x.startswith("hello"):
    print("$0")
else:
    print("$100")