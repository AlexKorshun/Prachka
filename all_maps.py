import random
class Engine():
    stop_tunneler = False
    def coinfliper(self):                                                                       #random range generation
        if random.randint(1,3)==1:
            return random.randint(2, self.rows)
        else:
            return random.randint(2,self.rows//2)

    def generateTheWay(self):
        self.stop_tunneler = True
        #the turning control field
        for y in range(self.rows):
            for x in range(self.columns):
                self.map[y][x] = 0
        finishPoint = [random.randint(1, self.rows - 2), random.randint(1, self.columns - 2)]
        self.map[finishPoint[0]][finishPoint[1]] = 7                                              #generate finish point
        self.direction = random.randint(1, 4)                                         #random direction generation
        currentPoint = finishPoint                                                       #variable for the current point
        stoper = 0
                                                #variable for the count of corners
        length = self.coinfliper()                                                              #variable for the length
        # verticaly = 11   horisontal = 10    both = 12
        start = True

        while stoper < 20:
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
                        if stoper < 10:
                            self.generateTheWay()
                            return
                        self.checker()
                        self.cleanTheWay()
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
                            if currentPoint[1]==1:
                                self.direction = 2
                            elif currentPoint[1]==self.columns-2:
                                self.direction = 1
                            else:
                                self.direction = random.randint(1, 2)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction==1:
                            if self.map[currentPoint[0]][currentPoint[1] + 1] != 0:
                                self.generateTheWay()
                                return

                            self.map[currentPoint[0]][currentPoint[1] + 1] = 99
                        else:
                            if self.map[currentPoint[0]][currentPoint[1] - 1] != 0:
                                self.generateTheWay()
                                return

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
                        if stoper < 10:
                            self.generateTheWay()
                            return
                        self.checker()
                        self.cleanTheWay()
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
                            if currentPoint[1] == 1:
                                self.direction = 2
                            elif currentPoint[1] == self.columns - 2:
                                self.direction = 1
                            else:
                                self.direction = random.randint(1, 2)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction==1:
                            if self.map[currentPoint[0]][currentPoint[1] + 1] != 0:
                                self.generateTheWay()
                                return

                            self.map[currentPoint[0]][currentPoint[1] + 1] = 99
                        else:
                            if self.map[currentPoint[0]][currentPoint[1] - 1] != 0:
                                self.generateTheWay()
                                return

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
                        if stoper < 10:
                            self.generateTheWay()
                            return
                        self.checker()
                        self.cleanTheWay()
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
                            if currentPoint[0] == 1:
                                self.direction = 3
                            elif currentPoint[0] == self.rows - 2:
                                self.direction = 4
                            else:
                                self.direction = random.randint(3, 4)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction == 3:
                            if self.map[currentPoint[0]-1][currentPoint[1]] != 0:
                                self.generateTheWay()
                                return
                            self.map[currentPoint[0]- 1][currentPoint[1] ] = 99
                        else:
                            if self.map[currentPoint[0]+1][currentPoint[1]] != 0:
                                self.generateTheWay()
                                return
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
                        if stoper < 10:
                            self.generateTheWay()
                        self.checker()
                        self.cleanTheWay()
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
                            if currentPoint[0] == 1:
                                self.direction = 3
                            elif currentPoint[0] == self.rows - 2:
                                self.direction = 4
                            else:
                                self.direction = random.randint(3, 4)
                        length = self.coinfliper()
                        stoper += 1
                        if self.direction == 3:
                            if self.map[currentPoint[0]-1][currentPoint[1]] != 0:
                                self.generateTheWay()
                                break

                            self.map[currentPoint[0] - 1][currentPoint[1]] = 99
                        else:
                            if self.map[currentPoint[0]+1][currentPoint[1]] != 0:
                                self.generateTheWay()
                                break
                            self.map[currentPoint[0] + 1][currentPoint[1]] = 99
        self.checker()
        self.cleanTheWay()


    def checker(self):
        we_have_7 = False
        for y in range(self.rows):
            for x in range(self.columns):
                if self.map[y][x] == 7:
                    we_have_7 = True
                    break
            if we_have_7:
                break
        if not we_have_7:
            print("нет 7")
            self.generateTheWay()


    def cleanTheWay(self):

        for y in range(self.rows):
            for x in range(self.columns):
                print(self.map[y][x], end = ' ')
            print()
        print()

        for y in range(self.rows):
            for x in range(self.columns):
                if self.map[y][x]==99:
                    self.map[y][x] = 1
                elif self.map[y][x]!=6 and self.map[y][x]!=7 and self.map[y][x]!= 1:
                    self.map[y][x] = 0
        currentPoint = [0, 0]
        for y in range(self.rows):
            for x in range(self.columns):
                if self.map[y][x] == 6:
                    currentPoint = [y,x]
                    print(currentPoint)
                    break
        self.stop_tunneler = False

        self.tunneler(1, currentPoint, 0)
        self.tunneler(2, currentPoint, 0)
        self.tunneler(3, currentPoint, 0)
        self.tunneler(4, currentPoint, 0)
    def tunneler(self, direction, lastpoint, count):

#где останавливался, там больше не останавливается вайб

        if self.stop_tunneler or count > 10:
            return
        currentPoint = lastpoint
        if direction==1:
            print("иду влево" + str(currentPoint), end=" ")
            while currentPoint[1]>0 and self.map[currentPoint[0]][currentPoint[1]-1]!=1 and self.map[currentPoint[0]][currentPoint[1]]!=7:
                currentPoint[1]-=1
            print("дошел до " + str(currentPoint))
            if self.map[currentPoint[0]][currentPoint[1]]==7:
                for i in self.map:
                    print(i)
                print("уебался" + " " + str(count))
                self.generateTheWay()
                return
            if currentPoint[1]>0:

                self.tunneler(3,currentPoint, count+1)
                self.tunneler(4, currentPoint, count+1)
            return
        elif  direction == 2:
            print("иду вправо" + str(currentPoint), end = " ")
            while currentPoint[1]<self.columns-1 and self.map[currentPoint[0]][currentPoint[1]+1]!=1 and self.map[currentPoint[0]][currentPoint[1]]!=7:
                currentPoint[1]+=1
            print("дошел до " + str(currentPoint))
            if self.map[currentPoint[0]][currentPoint[1]]==7:
                for i in self.map:
                    print(i)
                print("уебался" + " " + str(count))
                self.generateTheWay()
                return
            if currentPoint[1]<self.columns-1:
                self.tunneler(3,currentPoint, count+1)
                self.tunneler(4, currentPoint, count+1)
            return
        elif direction == 3:
            print("иду вниз" + str(currentPoint), end = " ")
            while currentPoint[0]<self.rows-1 and self.map[currentPoint[0]+1][currentPoint[1]]!=1 and self.map[currentPoint[0]][currentPoint[1]]!=7:
                currentPoint[0]+=1
            print("дошел до " + str(currentPoint))
            if self.map[currentPoint[0]][currentPoint[1]]==7:
                for i in self.map:
                    print(i)
                print("уебался" + " " + str(count))
                self.generateTheWay()
                return
            if currentPoint[1]<self.rows-1:
                self.tunneler(1,currentPoint, count+1)
                self.tunneler(2, currentPoint, count+1)
            return

        elif direction == 4:
            print("иду вверх" + str(currentPoint), end = " ")
            while currentPoint[0]>0 and self.map[currentPoint[0]-1][currentPoint[1]]!=1 and self.map[currentPoint[0]][currentPoint[1]]!=7:
                currentPoint[0]-=1
            print("дошел до " + str(currentPoint))
            if self.map[currentPoint[0]][currentPoint[1]]==7:
                for i in self.map:
                    print(i)
                print("уебался" + " " + str(count))
                self.generateTheWay()
                return
            if currentPoint[1]>0:
                self.tunneler(1,currentPoint, count+1)
                self.tunneler(2, currentPoint, count+1)
            return

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
        [0, 0, 1, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0]
    ]
'''