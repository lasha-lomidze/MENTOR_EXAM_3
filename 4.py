
# Write a function to generate Pascal's Triangle up to the specified number of rows.

def func(n):
    triangle = []  # ? vqmnit masivs
    for i in range(n):  
        row = [1]   # ? n-jer vqmnit axal masivs romelsac mtavar masivshi chavamtebt
        for j in range(1, i):
            row.append(triangle[i-1][j-1]+triangle[i-1][j])  # ? aq vitvlit shualedur mnishvnelobas (rac ricxvic unda chaisvas ), es logika ziustad ise mushaobs rogorc paskalis samkutxedis logika
        if i>0:
            row.append(1) # ? yoveli masivis boloshi unda iyos 1-iani
        triangle.append(row)
    return triangle



# test cases 4: 
print(func(1))
print(func(2))
print(func(3))
print(func(5))
print(func(0))

