start_char = ord('A')
num = 1

for i in range(5):
    if i % 2 == 0:
        for j in range(i + 1):
            print(chr(start_char), end=" ")
            start_char += 1
        print()
    else:
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()