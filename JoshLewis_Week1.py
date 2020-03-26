# INF322 Python
# Josh Lewis
# Week 1 – How To Defeat the Killer Rabbit of Caerbannog

print('Brother Maynard: On what count shalst thy lob the Holy Hand-grenade of Antioch?')
print('King Arthur: ')
answer = input()
while int(answer) != 3:
    print('Brother Maynard: The correct answer is 3, not ' + str(int(answer)) +
          '. To ' + str(int(answer) + 1) + ' shalt thou not count. ' +
          str(int(answer) + 2) + ' is right out! Once the number three, being' +
          ' the third number, be reached, then, lobbest thou thy Holy Hand Grenade' +
          ' of Antioch towards thy foe, who, being naughty in My sight, shall snuff it.')
    print('King Arthur: 1... 2... ' + str(int(answer)) + '!')
    print('Brother Maynard: Three, sir!')
    print('Enter 3: ')
    answer = input()
    
print('King Arthur: Three!')
print('BOOM!')
