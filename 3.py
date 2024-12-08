
# Write a function that takes a sentence and reverses the order of its words.


# ? funqcia ubralod yofs am winadadebas sityvebad shemdeg mat "step"-is gamoyenebit atrialebs da 
# ? sabolood aertebs am sityvebs joinis meshveobit
def func(s):
    words = s.split()
    rev = words[::-1]
    return " ".join(rev)


# test cases 3: 
print( func("Hello World") )
print( func("Python is great") )
print( func("a b c") )
print( func("") )
print( func(" Spaces ") )
