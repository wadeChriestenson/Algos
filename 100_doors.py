from time import sleep
doors = [False] * 101  # So we can start at door 1. We will ignore index 0

for i in range(1, 101):  # 101 because of how range works
    # for the second pass, x = 2, so we start at door 2, for the 3rd pass we start at door 3 etc.
    for j in range(i, 101, i):
        doors[j] = not doors[j]  # using `not` to invert the Boolean value

# Print out just the positions of the open doors
for i in range(1, 101):
    if doors[i] is True:  # Or just if doors[i]
        print('Door', i, 'opened |O|')
        sleep(0.5)
    else:
        print('Door', i, ' closed [X]')
        sleep(0.5)

