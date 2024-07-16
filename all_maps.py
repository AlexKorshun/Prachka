import random
class Engine():
    def coinfliper(self):                                                                       #random range generation
        if random.randint(1,3)==1:
            return random.randint(2, self.rows)
        else:
            return random.randint(2,self.rows//2)

    def generateTheWay(self):                                                                #the turning control field

        finishPoint = [random.randint(1, self.rows - 2), random.randint(1, self.columns - 2)]
        self.map[finishPoint[0]][finishPoint[1]] = 7                                              #generate finish point

        self.direction = random.randint(1, 4)                                         #random direction generation
        self.direction =1

        currentPoint = finishPoint                                                       #variable for the current point
        stoper = 0                                                                    #variable for the count of corners
        length = self.coinfliper()                                                              #variable for the length

        # verticaly = 11   horisontal = 10    both = 12
        start = True
        while stoper < 200:

            if self.direction == 4:
                if currentPoint[0] > 1 and length > 0 and (self.map[currentPoint[0] - 1][currentPoint[1]]==10 or self.map[currentPoint[0] - 1][currentPoint[1]]==0):
                    if self.map[currentPoint[0]][currentPoint[1]] == 10:
                        self.map[currentPoint[0]][currentPoint[1]] = 12

                    currentPoint[0] -= 1

                    if self.map[currentPoint[0]][currentPoint[1]] == 10:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    else:
                        self.map[currentPoint[0]][currentPoint[1]] = 11
                    length -= 1
                else:
                    if self.map[currentPoint[0]+1][currentPoint[1]]==99:
                        self.map[currentPoint[0]][currentPoint[1]] = 6
                        print('deadEnd')
                        return
                    elif self.map[currentPoint[0]][currentPoint[1]+1]!=99 and self.map[currentPoint[0]][currentPoint[1]+1]!=0 and self.map[currentPoint[0]][currentPoint[1]-1]!=99 and self.map[currentPoint[0]][currentPoint[1]-1]!=0 or self.map[currentPoint[0]][currentPoint[1]-1]==99 and self.map[currentPoint[0]][currentPoint[1]+1]==99:
                        if self.map[currentPoint[0]][currentPoint[1]]==12:
                            self.map[currentPoint[0]][currentPoint[1]] = 10
                        else:
                            self.map[currentPoint[0]][currentPoint[1]] = 0
                        currentPoint[0]+=1
                    else:
                        if self.map[currentPoint[0]][currentPoint[1]-1]==99 and self.map[currentPoint[0]][currentPoint[1]+1]==0:
                            self.direction = 2
                        elif self.map[currentPoint[0]][currentPoint[1]+1]==99 and self.map[currentPoint[0]][currentPoint[1]-1]==0:
                            self.direction = 1
                        else :
                            self.direction = random.randint(1, 2)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction==1:
                            self.map[currentPoint[0]][currentPoint[1] + 1] = 99
                        else:
                            self.map[currentPoint[0]][currentPoint[1] - 1] = 99

            elif self.direction == 3:
                if currentPoint[0] < self.rows-2 and length > 0 and (self.map[currentPoint[0] + 1][currentPoint[1]]==10 or self.map[currentPoint[0] + 1][currentPoint[1]]==0):
                    if self.map[currentPoint[0]][currentPoint[1]] == 10:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    currentPoint[0] += 1
                    if self.map[currentPoint[0]][currentPoint[1]] == 10:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    else:
                        self.map[currentPoint[0]][currentPoint[1]] = 11
                    length -= 1
                else:
                    if self.map[currentPoint[0]-1][currentPoint[1]]==99:
                        self.map[currentPoint[0]][currentPoint[1]] = 6
                        print('deadEnd')
                        return
                    elif self.map[currentPoint[0]][currentPoint[1]+1]!=99 and self.map[currentPoint[0]][currentPoint[1]+1]!=0 and self.map[currentPoint[0]][currentPoint[1]-1]!=99 and self.map[currentPoint[0]][currentPoint[1]-1]!=0 or self.map[currentPoint[0]][currentPoint[1]-1]==99 and self.map[currentPoint[0]][currentPoint[1]+1]==99:
                        if self.map[currentPoint[0]][currentPoint[1]]==12:
                            self.map[currentPoint[0]][currentPoint[1]] = 10
                        else:
                            self.map[currentPoint[0]][currentPoint[1]] = 0
                        currentPoint[0]-=1
                    else:
                        if self.map[currentPoint[0]][currentPoint[1]-1]==99 and self.map[currentPoint[0]][currentPoint[1]+1]==0:
                            self.direction = 2
                        elif self.map[currentPoint[0]][currentPoint[1]+1]==99 and self.map[currentPoint[0]][currentPoint[1]-1]==0:
                            self.direction = 1
                        else :
                            self.direction = random.randint(1, 2)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction==1:
                            self.map[currentPoint[0]][currentPoint[1] + 1] = 99
                        else:
                            self.map[currentPoint[0]][currentPoint[1] - 1] = 99


            elif self.direction == 2:
                if currentPoint[1] < self.columns - 2 and length > 0 and (
                        self.map[currentPoint[0]][currentPoint[1]+1] == 11 or self.map[currentPoint[0]][currentPoint[1]+ 1]  == 0):
                    if self.map[currentPoint[0]][currentPoint[1]] == 11:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    currentPoint[1] += 1
                    if self.map[currentPoint[0]][currentPoint[1]] == 11:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    else:
                        self.map[currentPoint[0]][currentPoint[1]] = 10
                    length -= 1
                else:
                    if self.map[currentPoint[0]][currentPoint[1]-1] == 99:
                        self.map[currentPoint[0]][currentPoint[1]] = 6
                        print('deadEnd')
                        return
                    elif self.map[currentPoint[0]+ 1][currentPoint[1] ] != 99 and self.map[currentPoint[0]+ 1][currentPoint[1] ] != 0 and self.map[currentPoint[0]- 1][currentPoint[1] ] != 99 and self.map[currentPoint[0]- 1][currentPoint[1] ] != 0 or self.map[currentPoint[0]- 1][currentPoint[1] ] == 99 and self.map[currentPoint[0]+ 1][currentPoint[1]] == 99:
                        if self.map[currentPoint[0]][currentPoint[1]] == 12:
                            self.map[currentPoint[0]][currentPoint[1]] = 11
                        else:
                            self.map[currentPoint[0]][currentPoint[1]] = 0
                        currentPoint[1] -= 1
                    else:
                        if self.map[currentPoint[0]-1][currentPoint[1]] == 99 and self.map[currentPoint[0]+1][currentPoint[1]] == 0:
                            self.direction = 3
                        elif self.map[currentPoint[0]+1][currentPoint[1]] == 99 and self.map[currentPoint[0]- 1][
                            currentPoint[1] ] == 0:

                            self.direction = 4
                        else:
                            self.direction = random.randint(3, 4)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction == 3:
                            self.map[currentPoint[0]- 1][currentPoint[1] ] = 99
                        else:
                            self.map[currentPoint[0]+ 1][currentPoint[1] ] = 99



            elif self.direction == 1:
                if currentPoint[1] > 1 and length > 0 and (
                        self.map[currentPoint[0]][currentPoint[1] - 1] == 11 or self.map[currentPoint[0]][currentPoint[1]- 1] == 0):
                    if self.map[currentPoint[0]][currentPoint[1]] == 11:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    currentPoint[1] -= 1
                    if self.map[currentPoint[0]][currentPoint[1]] == 11:
                        self.map[currentPoint[0]][currentPoint[1]] = 12
                    else:
                        self.map[currentPoint[0]][currentPoint[1]] = 10
                    length -= 1
                else:
                    if self.map[currentPoint[0]][currentPoint[1] + 1] == 99:
                        self.map[currentPoint[0]][currentPoint[1]] = 6
                        print('deadEnd')
                        return
                    elif self.map[currentPoint[0] + 1][currentPoint[1]] != 99 and self.map[currentPoint[0] + 1][currentPoint[1]] != 0 and self.map[currentPoint[0] - 1][currentPoint[1]] != 99 and self.map[currentPoint[0] - 1][currentPoint[1]] != 0 or self.map[currentPoint[0] - 1][currentPoint[1]] == 99 and self.map[currentPoint[0] + 1][currentPoint[1]] == 99:
                        if self.map[currentPoint[0]][currentPoint[1]] == 12:
                            self.map[currentPoint[0]][currentPoint[1]] = 11
                        else:
                            self.map[currentPoint[0]][currentPoint[1]] = 0
                        currentPoint[1] += 1
                    else:
                        if self.map[currentPoint[0] - 1][currentPoint[1]] == 99 and self.map[currentPoint[0] + 1][currentPoint[1]] == 0:
                            self.direction = 3
                        elif self.map[currentPoint[0] + 1][currentPoint[1]] == 99 and self.map[currentPoint[0] - 1][currentPoint[1]] == 0:
                            self.direction = 4
                        else:
                            self.direction = random.randint(3, 4)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction == 3:
                            self.map[currentPoint[0] - 1][currentPoint[1]] = 99
                        else:
                            self.map[currentPoint[0] + 1][currentPoint[1]] = 99


    def __init__(self):
        self.map = []
        self.columns = random.randint(9, 20)
        self.rows = random.randint(9, self.columns)
        for y in range(self.rows):
            self.map.append([])
            for x in range(self.columns):
                self.map[y].append(0)


maps = [
    [
        [0, 0, 1, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]
'''
     ,
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
'''