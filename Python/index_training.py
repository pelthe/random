word = str("")

for digit in "0165031806510":
    if digit == "0":
        digit = "x"
        word = word+digit
    else:
        word = word+digit
print(word)
