def get_fuel():

    while True:
        try:
           x,y = input("Fraction: ").split("/")
           x = int(x)
           y = int(y)
           percent = float(x/y*100)
           if percent > 100:
            continue
        except ValueError:
            print("x or y is not an integer")
        except ZeroDivisionError:
            print("Zero Division Error")
        else:
            return percent

def main():

    percent = get_fuel()

    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f'{percent:.0f}%')

main()