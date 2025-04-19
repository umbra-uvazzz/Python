from __future__ import annotations

from maths.greatest_common_divisor import greatest_common_divisor


def diophantine(a: int, b: int, c: int) -> tuple[int, int]: # ----Why float? You're solving for integers. These should be int, not float----
    """
    Diophantine Equation : Given integers a,b,c ( at least one of a and b != 0), the
    diophantine equation a*x + b*y = c has a solution (where x and y are integers)
    iff greatest_common_divisor(a,b) divides c.

    GCD ( Greatest Common Divisor ) or HCF ( Highest Common Factor )

    >>> diophantine(10,6,14)
    (-7, 14)

    >>> diophantine(391,299,-69)
    (9, -12)

    But above equation has one more solution i.e., x = -4, y = 5.
    That's why we need diophantine all solution function.

    """

    assert (
        c % greatest_common_divisor(a, b) == 0
    )  # greatest_common_divisor(a,b) is in maths directory
    (d, x, y) = extended_gcd(a, b)  # extended_gcd(a,b) function implemented below
    r = c // d # ----Added // instead of / to ensure integer division
    return (r * x, r * y)


def diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> list[tuple[int, int]]:
    """
    Lemma : if n|ab and gcd(a,n) = 1, then n|b.

    Finding All solutions of Diophantine Equations:

    Theorem : Let gcd(a,b) = d, a = d*p, b = d*q. If (x0,y0) is a solution of
    Diophantine Equation a*x + b*y = c.  a*x0 + b*y0 = c, then all the
    solutions have the form a(x0 + t*q) + b(y0 - t*p) = c,
    where t is an arbitrary integer.

    n is the number of solution you want, n = 2 by default

    >>> diophantine_all_soln(10, 6, 14)
    [(-7, 14), (-4, 9)]
    
    >>> diophantine_all_soln(10, 6, 14, 4)
    [(-7, 14), (-4, 9), (-1, 4), (2, -1)]
    
    >>> diophantine_all_soln(391, 299, -69, n=4)
    [(9, -12), (22, -29), (35, -46), (48, -63)]

    """
    (x0, y0) = diophantine(a, b, c)  # Initial value
    d = greatest_common_divisor(a, b)
    p = a // d
    q = b // d
    
    solutions = []
    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        solutions.append((x,y))
    return solutions


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers
    x and y, then d = gcd(a,b)

    >>> extended_gcd(10, 6)
    (2, -1, 2)

    >>> extended_gcd(7, 5)
    (1, -2, 3)

    """

    # ---- Your extended_gcd asserts a >= 0 and b >= 0. This is too restrictive — the algorithm works fine with negative integers. ----

    
    """
    assert a >= 0
    assert b >= 0
"""
    if b == 0:
        d, x, y = a, 1, 0
    elif a < 0 or b < 0:
        sign = (-1 if a < 0 else 1, -1 if b < 0 else 1)
        d, x, y = extended_gcd(abs(a), abs(b))
        return (d, x * sign[0], y * sign[1])
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0
    assert b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


if __name__ == "__main__":
    from doctest import testmod
"""
    testmod(name="diophantine", verbose=True)
    testmod(name="diophantine_all_soln", verbose=True)
    testmod(name="extended_gcd", verbose=True)
    testmod(name="greatest_common_divisor", verbose=True)
"""
    testmod(verbose=True)
