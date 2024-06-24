import datetime
import inflect
import sys

def get_bday()-> str:
    while(True):
        bdaystring = input("Birthday in YYYY-MM-DD format: ")

        try:
            year, month, day = bdaystring.split('-')
        except ValueError:
            sys.exit('Invalid date')
        except SystemExit:
            pass
        else:
            return year, month, day

def minutestowords(minutes):
    #create inflection engine
    p = inflect.engine()
    #use method to convert minutes into words
    words = p.number_to_words(minutes, andword = '')
    return f"{words.capitalize()} minutes"

def main():
    # get the date right now
    nowtime = datetime.date.today()
    #get users birthday
    year, month, day = get_bday()
    #convert string to int for insertion into datetime object
    year = int(year)
    month = int(month)
    if (month >12 or month < 1):
        raise ValueError
    day = int(day)
    if (day <1 or day >31):
        raise ValueError
    birthday = datetime.date(year,month,day)
    #subtract dates from one another to get elapsed time
    delta = nowtime - birthday
    #convert total seconds to minutes
    minutes = int(delta.total_seconds()//60)
    print(minutestowords(minutes))

if __name__ == "__main__":
    main()