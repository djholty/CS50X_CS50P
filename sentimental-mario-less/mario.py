# TODO


def main():
    height = get_height()

    for i in range(height):
        spaces = height - 1 - i
        hashes = i + 1
        for j in range(spaces):
            print(" ", end="")
        for k in range(hashes):
            print("#", end="")
        print()


# function to get valid height
def get_height():
    while True:
        # first make sure the use input is a number, if not reprompt
        try:
            height = int(input("Height: "))
        except:
            print("Incorrect input")
            continue
        # then if input is a number, make sure its between 1 and 8 inclusive
        else:
            if (height < 1 or height > 8):
                print("Incorrect input")
                continue
            else:
                break
    return height


main()