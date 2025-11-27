matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#to use indivisual elements you use 2 square brackets 0 is the first list but in zero the index value of 2 is 1 so print(matrix[0][1]) 
print(matrix[0][1])
print(matrix[2][2])

for row in matrix:
    for item in row:
        print(item)


print(matrix.index(1))
