def convert(a):
        a = a.replace(":)", "🙂")
        a = a.replace(":(","🙁" )
        return a

def main():
    x = input("type in a sentence: ")
    print(convert(x))

if __name__ == "__main__":
    main()