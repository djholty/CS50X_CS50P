groc = {}

while True:
    try:
        item = input().upper()
        groc[item] = groc.get(item, 0) + 1
    except KeyboardInterrupt:
        print()
        break
    except EOFError:
        print()
        break

for i in sorted(groc.keys()):
    print(groc[i], i )