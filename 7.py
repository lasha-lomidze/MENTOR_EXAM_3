
# Write a function that takes two integers, start and end, and returns a list of all prime numbers in the range [start, end]. 
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.

def func(a, b):

    # shevqmenit martivi logika romelic amowmebs martivi ricxvia tu ara
    def is_prime(n):
        count = 1
        for i in range(1, n):
            if n%i == 0:
                count+=1
        return count==2
         
    
    return [num for num in range(a, b + 1) if is_prime(num)] # martivi for loopis da ifis logika romelic gadauyveba ricxveba da amowmebs tu martivia, masivis formatshi
        
    

# test cases 7: 
print(func(10,20))
print(func(1, 10))
print(func(20, 30))
print(func(24, 25))
print(func(1, 1))

