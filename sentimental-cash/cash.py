from cs50 import get_float


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(f"{coins}")


# gets the change to be delivered
def get_cents():
    cents = get_float("Change: ")
    while (cents < 0):
        cents = get_float("Change: ")
    cents = int(100*cents)
    return cents


# calculates quarters from change first
def calculate_quarters(cents):
    coincount = 0
    while (cents >= 25):
        cents = cents - 25
        coincount = coincount + 1
    return coincount


# after quarters are pulled out then give as many dimes as you can
def calculate_dimes(cents):
    coincount = 0
    while (cents >= 10):
        cents = cents - 10
        coincount = coincount + 1
    return coincount


# do same for nickels next
def calculate_nickels(cents):
    coincount = 0
    while (cents >= 5):
        cents = cents - 5
        coincount = coincount + 1
    return coincount


# finally give rest of change as pennies
def calculate_pennies(cents):
    coincount = 0
    while (cents >= 1):
        cents = cents - 1
        coincount = coincount + 1
    return coincount


main()