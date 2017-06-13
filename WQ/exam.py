import sys
print("**********************************")
print("Question 31")
print("A loop that sums the numbers from 101 to 2033")
value = 0
for n in range(101,2033):
    value = value + n

print(value)

print("**********************************")
print("Question 32")
print('Using the string: \
 create a loop that sums \
 the numbers from 0 to the total number of \
 bytes this string occupies in memory')

string = "It is not the man who has too little, but the man who craves more, that is poor."
counter = 0
i = 0
while counter <= sys.getsizeof(string):
    i = i + counter
    print(counter)
    counter = counter + 1
