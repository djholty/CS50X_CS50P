import sys

if len(sys.argv) == 2:
    name, extension = sys.argv[1].split(".")
    if extension != "py":
        sys.exit("Not a python file")
    try:
        with open(sys.argv[1], 'r') as file:
            lines = 0
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.isspace():
                    continue
                #elif line.lstrip().startswith('"""'):
                    #continue
                else:
                    lines += 1
            print('Lines: ', lines)
    except (FileNotFoundError):
        print("File does not exist")
        sys.exit()
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit()