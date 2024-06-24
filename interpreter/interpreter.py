x = input("Expression: ")
a, b, c = x.split(" ")
a = float(a)
c = float(c)
def calc(a,b,c):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a*c
    elif b == "/":
        return a/c
print(calc(a,b,c))
