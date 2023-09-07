import secrets
import string

letter = string.ascii_letters
digits = string.digits
special_char = string.punctuation

alphabet = letter + digits + special_char

your_name = input("Enter your name: ")

pwd_length = 5

rp = 0

while rp == 0:

    while True:
        pwd = ""

        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if(any(char in special_char for char in pwd) and sum(char in digits for char in pwd)>=2):
            break

    pwd = your_name + pwd

    print(f"\n==> Your password: {pwd}")

    rp = input("\n0 = Reset \t 1 = OK: \nChoose 0 or 1: ")
    rp = int(rp)

print(f"The generated password is: {pwd}")

file = open("archivefiles.csv", "w", encoding="utf8")
message = input("Enter message: ")
file.write(message + "\n")
file.write(pwd)
file.close()

