cam = input("camelCase: ")
snake_case = ""
for c in cam:
    if c.isupper() == True:
        snake_case = snake_case + "_" + c.lower()
    else:
        snake_case = snake_case + c

print(snake_case)