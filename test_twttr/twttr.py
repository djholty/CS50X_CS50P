def main():
    x = input("Whats the tweet to shorten?")
    print(shorten(x))

def shorten(word):
    letterlist = []
    shortword = ""
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            continue
        else:
            letterlist.append(letter)
    for letter in letterlist:
        shortword += letter
    return shortword
if __name__ == "__main__":
    main()