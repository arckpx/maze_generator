import numpy as np
import matplotlib.pyplot as plt

# generate maze
WIDTH = 101
HEIGHT = 101
maze = np.zeros((HEIGHT, WIDTH))
maze[1, 1] = 0.7
pos = [1, 1]
poslist = [[1, 1]]
move = [0]

while poslist:

    # forward tracking
    while move:
        # pos = poslist[-1]
        # checking unexplored
        move = []
        if (pos[1] != 1) and (maze[pos[0], pos[1] - 2] == 0):
            move.append("l")
        if (pos[1] != WIDTH - 2) and (maze[pos[0], pos[1] + 2] == 0):
            move.append("r")
        if (pos[0] != 1) and (maze[pos[0] - 2, pos[1]] == 0):
            move.append("u")
        if (pos[0] != HEIGHT - 2) and (maze[pos[0] + 2, pos[1]] == 0):
            move.append("d")

        # choosing move
        if move:
            rand = np.random.randint(0, len(move))

            if move[rand] == "l":
                poslist.append([pos[0], pos[1] - 2])
                maze[pos[0], pos[1] - 1] = 1
                maze[pos[0], pos[1] - 2] = 1
                pos[1] -= 2
            if move[rand] == "r":
                poslist.append([pos[0], pos[1] + 2])
                maze[pos[0], pos[1] + 1] = 1
                maze[pos[0], pos[1] + 2] = 1
                pos[1] += 2
            if move[rand] == "u":
                poslist.append([pos[0] - 2, pos[1]])
                maze[pos[0] - 1, pos[1]] = 1
                maze[pos[0] - 2, pos[1]] = 1
                pos[0] -= 2
            if move[rand] == "d":
                poslist.append([pos[0] + 2, pos[1]])
                maze[pos[0] + 1, pos[1]] = 1
                maze[pos[0] + 2, pos[1]] = 1
                pos[0] += 2

    # backtracking
    while not move:

        poslist.pop(-1)
        if not poslist:
            break
        pos = poslist[-1]

        # checking unexplored
        if (pos[1] != 1) and (maze[pos[0], pos[1] - 2] == 0):
            move.append("l")
        if (pos[1] != WIDTH - 2) and (maze[pos[0], pos[1] + 2] == 0):
            move.append("r")
        if (pos[0] != 1) and (maze[pos[0] - 2, pos[1]] == 0):
            move.append("u")
        if (pos[0] != HEIGHT - 2) and (maze[pos[0] + 2, pos[1]] == 0):
            move.append("d")

plt.imshow(maze)
plt.show()
