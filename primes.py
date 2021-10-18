

def isprime(x):
    primebool = False
    for each in range(2, int(x**0.5)+1):

        if x % each == 0:
            return False
    return True


numtocheck = 17


primelist = []
for num in range(1, 100, 2):
    if isprime(num):
        primelist.append(num)

print(primelist)
