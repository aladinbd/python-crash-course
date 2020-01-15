squares = []
for value in range(1, 11):
    square = value ** 2 # double asterisk ** represent exponents
    squares.append(square)

print(squares)

# We can get same output omiting temporary variable
for value in range(1, 11):
    squares.append(value**2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
