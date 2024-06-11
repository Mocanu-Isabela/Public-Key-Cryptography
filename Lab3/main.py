# 2. Pollard’s ρ algorithm. The implicit function will be f(x) = x^2 + 1, but it will also allow the use of a function f given by the user.

def f(x, function):  # function that decides if f(x) uses the implicit function or one given by the user
    if function == "0":
        nr = (x ** 2 + 1) % n
    else:
        nr = function(x)
    return nr


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def pollard_rho(n, function):
    d = 1
    x = y = 2
    i = 0
    count = 0
    while d == 1:  # we run the algorithm while 1 < d < n
        # we compute the sequence: Xj = f (Xj−1) mod n
        x = f(x, function)
        y = f(f(y, function), function)
        i += 1
        # and d will be: d = (|X2j − Xj|, n)
        d = gcd(abs(x - y), n)
        print('(|x' + str(i) + ' - y' + str(i) + '|, n) = ' + str(d))
        count += 1
        if count > 500:  # we stop if we computed d more that 500 times
            print('Count reached 500')
            break
        if d == n:  # we stop if d is equal to n
            print('d = n => FAILURE :(')
            return
    print('n = ' + str(d) + ' * ' + str(n // d))


if __name__ == '__main__':
    fun = input("f = ")
    if fun != "0":
        function = eval('lambda x: ' + fun)
    else:
        function = "0"
    n = 2 ** 499 - 1
    # n = 187
    # n = 27
    pollard_rho(n, function)
