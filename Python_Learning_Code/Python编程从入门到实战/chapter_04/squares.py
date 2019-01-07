squares = []
for value in range(1, 11):
    square = value ** 2  # value*value
    squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
