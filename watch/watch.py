
import re
import sys

def main():
    html = input('HTML: ')
    try:
        print(parse(html))
    except:
        pass

def parse(html: str)-> str:
    matches = re.findall(r'http(?:s)?\://(?:www\.)?youtube\.com/embed/(.*?)"', html, flags = re.DOTALL)
    if len (matches) >= 1:
        return f"https://youtu.be/" + matches[0]
    else:
        return None

    #alternative option
    #matches = re.finditer(pattern, html)
    # for match in matches:
    #     code = match.group(1)
    # return f"https://youtu.be/"+code


if __name__ == "__main__":
    main()