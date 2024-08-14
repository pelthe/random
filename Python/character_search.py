email = str("")
for ch in "heikki.smith@pythoninstitute.org":
    if ch == "@":
        print(email)
        break
    else:
        email = email+ch
