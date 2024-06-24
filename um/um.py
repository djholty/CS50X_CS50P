
import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r'\bum\b'
    m = re.findall(pattern,s, re.IGNORECASE)
    return len(m)

if __name__ == "__main__":
    main()