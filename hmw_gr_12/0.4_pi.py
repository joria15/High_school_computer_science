# Exercise 4: Challenge
def approximate_pi(n):
    """
        Approximates the value of pi using the Leibniz series:
        pi ≈ 4/1 - 4/3 + 4/5 - 4/7 + ...

        Arg: n (int) - Number of terms to include in the approximation.

        Returns (float): Approximated value of pi.
        """
    term = 0
    for i in range(n):
        pi = ((-1)**i)*(4 / (2*i+1))
        term += pi
    return term


# Test cases for approximate_pi
print(approximate_pi(3))     # Expected: 3.466666666666667
print(approximate_pi(10))    # Expected: 3.0418396189294032
print(approximate_pi(100))   # Expected: 3.1315929035585537
print(approximate_pi(1000))  # Expected: 3.140592653839794