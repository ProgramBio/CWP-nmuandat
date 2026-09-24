user_input = input()

for char in user_input:
    if char.islower():
        print(char.upper(), end="")
    else:
        print(char.lower(), end="")