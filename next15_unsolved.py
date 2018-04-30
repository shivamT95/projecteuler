import os
solved = []
for x in os.listdir('.'):
    if os.path.isdir(x) and x[0] == 'Q':
        solved.append(int(x[1:]))
unsolved = []
for x in range(1,500):
    if x not in solved:
        unsolved.append(x)
        if len(unsolved)>=15:
            break
print(unsolved)
