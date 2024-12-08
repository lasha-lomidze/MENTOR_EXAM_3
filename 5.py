
# Write a function to encrypt strings using a Caesar cipher with a given shift value.

def func(text, shift):
    result = ""  # shevqmnat rasac davabrunebt sabolood
    for char in text:   # gadavuyvet rom movaxdinot yvela asoze operacia
        # didi da patara asos logika igivea ubralod unikodis sxvadasxva adgilas iwyeba
        if char.isupper():   
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) 
        elif char.islower():    
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # am logikit viyenebt unikods romvimodzraot anbanis shignit shiftis mixedvit, sabolood 26 vnashtavt radgan amdeni asoa inglisur alfabetshi
        else:
            # tu aso ar aris da nishania ubralod vamatebt
            result += char
    return result


print(func("abc", 2))
print(func("xyz", 3))
print(func("Hello, World!", 5))
print(func("Python", 0))
print(func("abc", -1))