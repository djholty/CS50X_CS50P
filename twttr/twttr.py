#place in twttr.py
def main():
    x = input("Whats the tweet to shorten?")
    print(shorten(x))
    sys.exit(0)

def shorten(word):
    shortword = ""
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            continue
        else:
            shortword += letter
    return shortword

if __name__ == "__main__":
    main()