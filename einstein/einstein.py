#from scipy import constants

def energy(m):
    c = 300000000
    e = m * c**2
    return e


x = int(input("Please enter a mass in kg: "))
print(energy(x))