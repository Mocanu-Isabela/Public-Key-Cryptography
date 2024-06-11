# 7. Algorithm for determining all Carmichael numbers less than a given bound.

from math import gcd

def carm_math_reorder(num):
    if gcd(2, num) == 1 and all(gcd(k, num) == 1 for k in range(3, int(round(num**0.5)), 2)):  # we verify if the number is prime
        return 'Prime'
    elif gcd(num, 2) == 1 and all(pow(b, num, num) == b for b in range(1, num)):  # we verify if the number is a Carmichael number using this formula b^n % n = b, for all integers b which are relatively prime to n
        return 'Carmichael'
    return 'Composite'  # otherwise, it is a composite number


if __name__ == '__main__':
    nr = int(input("nr = "))
    CarmichaelNumbers = []
    for x in range(nr):
        if carm_math_reorder(x) == 'Carmichael':
            CarmichaelNumbers.append(x)

    print("The Carmichael numbers smaller than ", nr, " are: ")
    for C_nr in CarmichaelNumbers:
        print(C_nr)

