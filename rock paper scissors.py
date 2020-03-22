import random, string
inte = random.randint(0,2)
playerMove = input('Rock, Paper, or Scissors?').lower
if playerMove == 'rock':
    pMoveNo = 0
elif playerMove == 'paper':
    pMoveNo = 1
elif playerMove == 'scissors':
    pMoveNo = 2
else:
    print ('try again')
print('you played ' , pMoveNo)
print('ai played ' , inte)
if pMoveNo == inte:
    print('tie')
elif pMoveNo == inte + 1:
    print ('you win')
elif inte == pMoveNo + 1:
    print ('you lose')
else:
    print ('wtf')
