a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
user_input = int(input('Select a number: \n'))
[b.append(i) for i in a if i < user_input]
print(b)