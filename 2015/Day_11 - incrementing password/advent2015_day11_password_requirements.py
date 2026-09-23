alphabet = "abcdefghijklmnopqrstuvwxyz"
index = 7
check = False


def increment(word, i):
    letter = word[i]
    alpha_index = (alphabet.index(letter) + 1) % 26
    if i == 7:
        left = word[:7]
        right = ""
    elif i == 0:
        left = ""
        right = word[1:]
    else:
        left = word[:i]
        right = word[i + 1:]
    new_password = str(left + alphabet[alpha_index] + right)
    if alpha_index == 0:
        new_password, i = increment(new_password, i - 1)
        i += 1
    return new_password, i


def password_check(word):
    check = False
    check1 = False
    check2 = False
    check3 = False
    for i in range(24):
        test = alphabet[i:i + 3]
        if test in word:
            check1 = True
    if "i" not in word and "o" not in word and "l" not in word:
        check2 = True
    pairs = 0
    i = 1
    while i < len(word):
        if word[i] == word[i - 1]:
            pairs += 1
            if i < len(word) - 1:
                i += 1
        i += 1
    if pairs >= 2:
        check3 = True
    if check1 and check2 and check3:
        check = True
    return check


# password changed for part 2

password = "cqjxxyzz"
while not check:
    password, index = increment(password, index)
    check = password_check(password)
print(password)
