

# 1. Check If Two Strings Are Anagrams
# Task:
# Write a function that determines if two strings are anagrams of each other.

# es funqcia tavistavad gamoricxvas spacebs da did asoebs gadaaqcevs patarad, shemdeg alfabetis mixedvit dalagebul
# sityvebis asoebs sheadarebs da tavsitavad amit tavadgent tu es ori sityva anagramia
def func1(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a)==sorted(b)

# 1) test cases
print( func1("listen", "silent") )
print( func1("triangle", "integral") )
print( func1("apple", "pale") )
print( func1("a", "a") )
print( func1("rat", "car") )
