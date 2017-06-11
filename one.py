print("A simple spelling program using while loop")
name = input("Please enter a name: ")
counter = 0  # A counter to keep track of number of loops
while counter <= len(name) - 1:  # Has to eventually evaluate to false
    print("There is a", name[counter], "in", name)
    counter = counter + 1
