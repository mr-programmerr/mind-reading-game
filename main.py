import random
n = random.choices([3, 5, 7])
k = random.choices([4, 6])
print("\n - - - - -\nWelcome to the Mind Reading game.\nTo Start select one of the numbers (not letters) shown below,\n"
      "and keep it in mind.\n")
tab1 = [['', 'a', '1', 'b'],
        ['', '2', 'c', '3'],
        ['', 'd', '4', 'e']]


# this function prints the table and asks for the user to press enter to continue
def table():
    for i in tab1:
        for z in i[:3]:
            print(z, end=' ')
        for z in i[-1]:
            print(z)
    print("\nPress Enter to continue\n - - - - - ")
    input()


table()

# ask the user to move k steps
print("Now starting from the number you chose, move", k, "steps\n"
      "*** RULES: You can move UP & Down and Left & Right, But YOU CANNOT MOVE DIAGONALLY ***\n")
table()

# remove letter 'e' from the table
tab1[2][3] = ''

# tell the user that e has been removed
print("I have a feeling that you are not on letter 'e'. So I am going to remove it :)")
table()

# ask the user to move n steps
print("Now move", n, "steps\n"
      "*** Reminder: You can move UP & Down and Left & Right, But YOU CANNOT MOVE DIAGONALLY ***\n")
table()

# remove number '3'
tab1[1][3] = ' '

# tell the user that 3 has been removed
print("I guess you are not on number '3'. So I am removing it :)")
table()

# ask the user to move n steps
print("Now move", k, "steps\n")
table()

# remove number '4'
tab1[2][2] = ' '

# tell the user that 4 has been removed
print("Let me remove '4' because you are not on it, are you? :)")
table()

# ask the user to move k steps
print("Now move", n, "steps\n"
      "*** Reminder: You can move UP & Down and Left & Right, But YOU CANNOT MOVE DIAGONALLY ***\n")
table()

# remove b and d
tab1[0][3] = ' '
tab1[2][1] = ' '

# tell the user that b and d have been removed
print("It is getting harder! but I feel like you are not on 'b' or 'd' :)")
table()

# ask the user to move 1 step
print("Now move [3] steps\n")
table()

# remove 1
tab1[0][2] = ' '

# tell the use that 1 has been removed
print("'1' has been removed. It is time for the final step :)")
table()

# ask the user to move 3 steps
print("For the last time, move [1] step\n")
table()

# remove a and c
tab1[0][1] = ' '
tab1[1][2] = ' '

# tell the user that he ended up on number 2
print("*** You ended up on number [2[. Am I right? ***")
