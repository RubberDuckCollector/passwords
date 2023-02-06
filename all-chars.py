from random import randint

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`\"\'\|[]-=_+~!@£$%^&*(),./<>?#€"

num_of_chars = int(input("How many characters long should the password be? "))

password = ""
for i in range(num_of_chars):
    # add random char
    rand_char = randint(0, len(alphabet)-1)
    password += alphabet[rand_char]

print(password)
