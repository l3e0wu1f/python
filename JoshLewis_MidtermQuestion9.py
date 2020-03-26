# Create a list with 5 indexes. Set this list to variable myList. Make up data.
myList = ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Jones']

# Create a dictionary with 5 keys/values. Set this dictionary to variable myDict.  Make up data.
myDict = {'Graham Chapman': 'King Arthur', 'Eric Idle': 'Sir Robin, the Not-Quite-So-Brave-as-Sir-Lancelot', 'John Cleese': 'Sir Lancelot, the Brave', 'Michael Palin': 'Sir Galahad, the Pure', 'Terry Jones': 'Sir Bedevere, the Wise'}

# Write a function that will print the contents of the list, one index per line.
def printList():
    for name in myList:
        print(name + '\n')

# Write a function that will print the contents of the dictionary, format the output to reflect one key:value per line with a colon between.
def printDict():
    for k, v in myDict.items():
        print(k, ': ', v)

# Write a function that will take a list and a dictionary, then insert the dictionary into the list, in the 3rd index slot and return the new list.
def listInsert():
    myList.insert(2, myDict)
    return myList

# Write a function that will take a list, then change the first two indexes to be 'roger' and 'dodger'. Next, slice a list and only return the last three indexes as a new list.
def listChanger():
    myList.insert(0, 'roger')
    myList.insert(1, 'dodger')
    newList = myList[-3:]
    return newList

# Execute each function, making sure to print the last two as they are returns.
print("Question 3: \n")
printList()
print("Question 4: \n")
printDict()
print("Question 5: \n")
print(listInsert())
print("Question 6: \n")
print(listChanger())
