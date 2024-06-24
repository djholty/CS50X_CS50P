def convert(fraction: str)-> int:

        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y != 0 and x > y:
                raise ValueError("X can't be greater than Y")
            percent = float(x/y*100)

        except (ValueError, ZeroDivisionError):
            raise
        return int(percent)

def gauge(percentage: int)-> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"





#def get_fuel():


def main():
    fraction = input("fraction: ")
    percentage = convert(fraction)
    print("Percentage",percentage)
    level = gauge(percentage)
    print("Level:",level)

if __name__ == "__main__":
    main()