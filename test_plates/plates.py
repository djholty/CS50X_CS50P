def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#does the plate start with two letters
def startwolet(a):
    a = a[0:2]
    if a.isalpha() == True:
        return True
    else:
        return False
# is the plate less than 6 characters and 2 or more
def platelengood(a):
    if len(a) <=6 and len(a) >= 2:
        return True
    else:
        return False
#####################
#does the plate have digits?
def hasdigits(a):
    digpresent = None
    for c in a:
        if c.isdigit() == True:
            return True
    return False
#location of the first number
def loc_first_num(a):
    for i,c in enumerate(a):
        if c.isdigit() == True:
            return i

def is_alphanumeric(s):
    if s.isalnum():
        return True
    else:
        return False

#are all the numeric characteristics valid?
def apprnums(a):
    if hasdigits(a) == False:
        return True
    elif hasdigits(a) == True:
        if a[-1].isdigit() == False:#last digit must be a number if numbers are used
            return False
        if a[loc_first_num(a)] == "0": # first digit cannot be 0
            return False
        if a[loc_first_num(a):].isdigit() == False: # all characters after the first one must be digits
            return False
        else:
            return True
    else:
        return True
##################
#are there any inappropriate characters?
def apprpunc(a):
    for c in a:
        if c in [".", " ", "!", "?", "-"]:
            return False
        else:
            continue
    return True
#validator that calls all individual validators
def is_valid(s):
    if startwolet(s) == True and platelengood(s) == True and apprpunc(s) == True and apprnums(s) == True and is_alphanumeric(s) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()