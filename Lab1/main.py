import time

# we verify if x or y is 0, then we compute the gcd using the euclidean algorithm
def gcd_euclidean(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    r = x % y
    while r:
        x = y
        y = r
        r = x % y
    return y


# we verify if y is 0 (we check if x is 0 later, when the function goes once in the recursive step with y now being our
# initial x), then we compute the gcd using a recursive algorithm (it is very similar to the euclidean algorithm)
def gcd_recursive(x, y):
    if (y == 0):
        return x
    else:
        return gcd_recursive(y, x % y)


# we verify if x or y is 0, then we compute the gcd by finding which number is smaller and then looping through the
# range of numbers between 1 and the smaller number, when we reach a number that is divisor to both numbers (x and y)
# we say that is our gcd, after we parsed the ranged the last gcd obtained is the gcd
def gcd_using_loops(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    gcd = 1
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd


if __name__ == '__main__':
    input_set = [(16, 10), (31, 15), (100, 35), (144, 600), (201, 13), (44, 66), (792, 144), (279720, 5769225),
                 (6930, 48024900), (5 ** 10, 50 ** 5), (6 ** 13, 8 ** 13)]
    print("\n")
    for input in input_set:
        x = input[0]
        y = input[1]
        print("        x = {},y = {}\n".format(x, y))

        print("GCD Eucliden Version :")
        start_time = time.time()
        gcd = gcd_euclidean(x, y)
        end_time = time.time()
        print("Time: {} seconds".format(end_time - start_time))
        print("Gcd is : {}\n".format(gcd))

        print("GCD Recursive Version :")
        start_time = time.time()
        gcd = gcd_recursive(x, y)
        end_time = time.time()
        print("Time: {} seconds".format(end_time - start_time))
        print("Gcd is : {}\n".format(gcd))

        print("GCD Loops Version :")
        start_time = time.time()
        gcd = gcd_using_loops(x, y)
        end_time = time.time()
        print("Time: {} seconds".format(end_time - start_time))
        print("Gcd is : {}\n".format(gcd))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
