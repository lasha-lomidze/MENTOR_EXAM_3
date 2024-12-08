# Write a function that generates the Xbonacci sequence. The Xbonacci sequence is a generalization of the Fibonacci sequence, where each number is the sum of the previous X numbers in the sequence.
# For example, if X = 3 and the initial sequence is [1, 1, 1], the sequence will proceed as follows:
# The 4th number is the sum of the previous 3: 1 + 1 + 1 = 3.
# The 5th number is the sum of the previous 3: 1 + 1 + 3 = 5.
# The 6th number is the sum of the previous 3: 1 + 3 + 5 = 9.
# Your function should take two arguments:
# X: The number of previous terms to sum.
# n: The number of terms to generate.


def func(x, n):
    # dasawyisi ( inicilaziacia masivis )
    seq = [1]*x

    # sanam gamovimushavebt n-cals gavagrdzelot
    while len(seq) < n:
        # aq vumateb wina "x" ricxvs rom mivigho shemdegi ricxvio chasasmelad (a)
        a = sum(seq[-x:])
        seq.append(a)

    return seq[:n]


# test cases BONUS:
print(func(3, 10))
print(func(2, 10))
print(func(4, 6))
print(func(5, 8))
print(func(3, 1))