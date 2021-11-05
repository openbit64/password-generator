import random
import clipboard

lowercase = 'abcedfghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
digits = '1234567890'
chars = '~`!#@$%^&*()-_+=""<>,.?/|'

l1 = []
l2 = []
l3 = []
l4 = []


for p in lowercase:
    l1.append(p)

for q in uppercase:
    l1.append(q)

for r in digits:
    l1.append(r)

for s in chars:
    l1.append(s)

all_list = l1 + l2 + l3 + l4
password = ''
length = int(input("Enter password length: "))

for i in range(length):
    k = random.choice(all_list)
    password += str(k)

clipboard.copy(password)
print(f"Generated password: {password} ")
print("Password copied to your clipboard!")