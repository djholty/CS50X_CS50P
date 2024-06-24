

def main():
    user_string = input("Please input your text to assess it's grade level: ")
    lettercounter = 0
    wordcounter = 0
    sentencecounter = 0

    # iterate through the characters and count the alphabetical characters
    for letter in user_string:
        if (letter.isalpha()):
            lettercounter += 1

    # split the string into a list of words separated by a space, get count of words
    wordlist = user_string.split(" ")
    wordcounter = len(wordlist)

    # print(f"{lettercounter}")
    # print(f"{wordcounter}")

    # find the number of sentences in the string

    for character in user_string:
        if (character == '.' or character == '!' or character == '?'):
            sentencecounter += 1

    # print(f"Sentence Counter: {sentencecounter}")

    # calculate the components of the coleman liau index and cast to float to avoid integer rounding errors
    L = ((lettercounter * 1.0) / wordcounter) * 100
    # printf("L is equal to %f\n", L)
    S = ((sentencecounter * 1.0) / wordcounter) * 100
    # printf ("F is equal to %f\n", S)
    index = (.0588 * L) - (.296 * S) - 15.8
    # print(f"Index: {index}")
    rounded_index = round(index)
    # print(f"Rounded Index: {rounded_index}")

    # output grade level based on the rounded index to the nearest grade level
    if (rounded_index < 1):
        print("Before Grade 1")
    elif (rounded_index == 1):
        print("Grade 1")
    elif (rounded_index == 2):
        print("Grade 2")
    elif (rounded_index == 3):
        print("Grade 3")
    elif (rounded_index == 4):
        print("Grade 4")
    elif (rounded_index == 5):
        print("Grade 5")
    elif (rounded_index == 6):
        print("Grade 6")
    elif (rounded_index == 7):
        print("Grade 7")
    elif (rounded_index == 8):
        print("Grade 8")
    elif (rounded_index == 9):
        print("Grade 9")
    elif (rounded_index == 10):
        print("Grade 10")
    elif (rounded_index == 11):
        print("Grade 11")
    elif (rounded_index == 12):
        print("Grade 12")
    elif (rounded_index == 13):
        print("Grade 13")
    elif (rounded_index == 14):
        print("Grade 14")
    elif (rounded_index == 15):
        print("Grade 15")
    elif (rounded_index == 16):
        print("Grade 16")
    elif (rounded_index > 16):
        print("Grade 16+")


main()