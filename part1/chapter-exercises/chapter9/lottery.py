import random

options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

my_ticket = [1, 2, 'B', 7]

count = 0
while True:
    winner = []
    for x in range(4):
        won = random.choice(options)
        winner.append(won)
    count += 1
    if winner == my_ticket:
        break

if count == 1:
    print(f'Wow... you just won the lottery!')
else:
    print(f'It took {count} attempts to match the winning ticket.')