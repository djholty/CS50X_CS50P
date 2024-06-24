cost = 50
while True:
    print("Amount due: ", cost)
    x = input("Insert Coin: ")
    if x in ["25", "10", "5"]:
        cost = cost - int(x)
    if cost <= 0:
        print("Change owed: ", abs(cost))
        break
