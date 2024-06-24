import re
import sys

def main():
    time = input('Hours: ')
    #if " to " not in input:
    #    raise ValueError
    print(convert(time))

def convert(s: str)-> str:
    try:
        pattern = r"(\d{1,2})(?::(\d\d))? (am|AM|PM|pm|..)(.{1,4})(\d{1,2})(?::(\d\d))? (am|AM|PM|pm|..)"
        matches = re.search(pattern, s)

        #save matched groups in values for hour, minute, am/pm for two times
        values = matches.groups('0')
        #I could have saved myself some trouble by doing matches.group('0') which would have automatically
        #replaced the None with 0, but i only learned of it after
        #also would remove the need for conversion from a tuple to a list
        #convert values to list from tuple, then
        # go through the list and if None is in the minutes, then replace with


        #print(values)
        h1, m1, ampm1, to, h2, m2, ampm2 = values
        if to != ' to ':
            raise ValueError('Should be " to "')
            sys.exit()
        # print(m1)
        # print(m2)
        m1 = int(m1)
        m2 = int(m2)
        if m1 > 59 or m2 > 59:
            raise ValueError("Invalid Input, time must be 59 or less")
            sys.exit()
       # if  ( ((ampm1 != ('AM' or 'PM')) or (ampm2 != ('AM' or 'PM')) ):
       #     raise ValueError('Invalid time format')
        #if its the morning/AM, but not 12AM, or if its 12 PM, return the hour without modifying it
        if (ampm1 == 'AM' and h1 != '12') or (h1 =='12' and ampm1 == 'PM'):
            h1 = int(h1)
            #print(h1)
            time1 = f"{h1:02}:{m1:02}"
        # if its 12 AM, it's a special case, and convert to 00 hours
        elif ((ampm1 == 'AM') and (h1 =='12')):
            time1 = f"00:{m1:02}"
        # for all the other PM cases add 12 to the hour
        else:
            h1 = int(h1) + 12
            #print(h1)
            time1 = f"{h1:2}:{m1:02}"

        #if its the morning/AM, but not 12AM, or if its 12 PM, return the hour without modifying it
        if (ampm2 == 'AM' and h2 != '12') or (h2 =='12' and ampm2 == 'PM'):
            h2 = int(h2)
            time2 = f"{h2:02}:{m2:02}"
        # if its 12 AM it's a special case and t to convert to 00 hours
        elif (ampm2 == 'AM' and h2 =='12'):
            time2 = f"00:{m2:02}"
        # all the other PM cases add 12 to the hour
        else:
            h2 = int(h2) + 12
            time2 = f"{h2:02}:{m2:02}"
    except AttributeError:
        raise ValueError("Invalid Input")
        sys.exit()

    return f'{time1} to {time2}'


if __name__ == "__main__":
    main()
