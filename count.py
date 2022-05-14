import random
import pyperclip

MAX_INT = 91093281

#https://stackoverflow.com/a/22808285 
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def main():
    to_reach = int(input("Enter a number:"))
    n1 = random.randint(1, MAX_INT)
    n2 = random.randint(1, MAX_INT)

    prod = n1*n2
    n3 = largest_prime_factor(prod)
    quotient = prod/n3


    n4 = random.randint(1, MAX_INT)
    summed = quotient + n4
    n5 = summed - to_reach

    return f"{int(n1)}*{int(n2)}/{int(n3)}+{int(n4)}-{int(n5)}"

while True:
    pyperclip.copy(main())
