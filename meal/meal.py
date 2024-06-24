def main():
    time = input("What time is it? ")
    ctime = convert(time)
    if (ctime >= 7 and ctime <= 8):
        print("breakfast time")
    elif (ctime >= 12 and ctime <= 13):
        print("lunch time")
    elif (ctime >= 18 and ctime <=19):
        print("dinner time")
    else:
        return None

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    time = hours + minutes
    return time

if __name__== "__main__":
    main()