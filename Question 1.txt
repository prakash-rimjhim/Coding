Reverse a given positive integer.
	123 => 321
	560 => 65
	1   => 1

*******CODE********


def solve():

    t = int(input())
    rev = 0

    while t !=0:
        digit = t % 10
        rev = rev *10 + digit
        t //=10

    print(rev)

solve()

