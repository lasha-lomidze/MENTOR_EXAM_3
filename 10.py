


# Write a function that sums two fractions and returns the result in its simplest form. The fractions will be given as two tuples, where each tuple consists of two integers: the numerator and the denominator. To simplify the result, you need to compute the Least Common Multiple (LCM) and Greatest Common Divisor (GCD) of the denominators.
# Then, simplify the result by dividing both the numerator and denominator by their GCD.


# vqmnit funqciebs - gcd, lcm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# mtavari funqcia ( es funqcia ubralod pirdapiri mnishvnelobit miyveba instruqcias )
def func(a, b):
    # shevqmnat cvladebi argumentebisgan 
    num1, den1 = a
    num2, den2 = b
    
    # gamoctvalot lcm "denominatorenbis"
    common_den = lcm(den1, den2)

    # gadavaqciot nawilebi rom qondet igive "denpominatori"
    num1 = num1*(common_den // den1)
    num2 = num2*(common_den // den2)

    # davamatot ertmanets numeratorebi
    res_num = num1+num2
    res_den = common_den

    # gavamartivot rezultati (bolo nawili)
    common_gcd = gcd(res_num, res_den)
    res_num //= common_gcd
    res_den //= common_gcd

    return (res_num, res_den)




# test cases 10: 
print(func((1,2), (1,3)))
print(func((1,4), (1,4)))
print(func((2,5), (1,5)))
print(func((3,4), (5,6)))
print(func((5,12), (7,15)))

