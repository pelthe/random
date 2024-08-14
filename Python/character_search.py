email = str("")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        print(email)
        break
    else:
        email = email+ch
