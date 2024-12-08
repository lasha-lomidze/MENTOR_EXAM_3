
# Write a function that calculates the primorial of a number. The primorial of a number n is the product of all prime numbers less than or equal to n. For example, the primorial of 5 is the product of the primes less than or equal to 5: 2 * 3 * 5 = 30.
# Your function should take an integer n and return the primorial of that number.


# martivi logika ormelic amowmebs tu ricxvi martivia
def is_prime(n):
        count = 1
        for i in range(1, n):
            if n%i == 0:
                count+=1
        return count==2


# funqcia romelic gadauyveba n-s da sheamowmebs da shasrulebns shesabamis operacias tu martiv ricxvs ipovis
def func(n):
    product = 1
    for i in range(2, n+1):
         if is_prime(i):
            product *= i
    return product

# test cases 9:
print(func(5))
print(func(10))
print(func(1))
print(func(7))
print(func(11))

