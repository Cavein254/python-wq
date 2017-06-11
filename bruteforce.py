import string
alphabet = string.ascii_lowercase[:]
alphabet = alphabet + string.ascii_uppercase[:]
alphabet = alphabet + "0,1,2,3,4,5,6,7,8,9"
print(alphabet)
passd = str.lower(input("Please enter you password: "))
rpass = []
counter = 0
i = 0
j = 0
while counter < len(passd):
    if alphabet[i] == passd[j]:
        rpass.append(passd[j])
        i = 0
        j += 1
        counter += 1
    else:
        i += 1

print(rpass)

