
# Write a function that counts the number of unique words in a string, 
# ignoring case sensitivity and punctuation.


# ? es funqcia jer gamoricxavs nebismier wertils mdzimes da eget punktuacias
# ? shemdeg did asoebs gadavaqcev patarad da yvela sityvas gavxdi unikalurs setad gadaqcevit
# ? vinaidan setshi ar sheidzleba ertze meti erti da igive elementi iyos
# ? sabolood vabruneb am unikaluri setis sigrdzes
def func(text):
    punctuation = ".,!?;:'\"()[]{}"
    for char in punctuation: 
        text = text.replace(char, "")
    text = text.lower()
    words = text.split()
    ans = set(words) 
    return len(ans)


# test cases 2:
print(func("The quick brown fox jumps over the lazy dog"))
print(func("Hello hello world!"))
print(func(""))
print(func("Python is fun. Python is cool."))
print(func("One word"))