from functools import reduce

word = 'WHEN YOU PLAY IN THE GAME OF THRONES YOU WIN OR YOU DIE'

print(reduce(lambda x,y:x+y, map(lambda x:x, word)))