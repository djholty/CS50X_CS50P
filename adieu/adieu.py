import inflect
p = inflect.engine()

message = "Adieu, adieu, to"
names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
    except KeyboardInterrupt:
        break
mylist = p.join(names)
print(message, mylist)