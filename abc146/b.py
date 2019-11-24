N = int(input())
S = input()
chars = []
for c in S:
    newC = chr((((ord(c) - 65) + N) % 26) + 65)
    chars.append(newC)
print("".join(chars))