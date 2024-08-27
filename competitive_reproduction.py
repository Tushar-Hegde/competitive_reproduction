import random
from colored import fg

black = fg('black')
blue = fg('blue')
red = fg('red')
white = fg('white')
green = fg('green')


class Matrix():
    def __init__(self):
        self.matrix = {}
        self.two_plants = 0
        self.four_plants = 0
        self.parasites = 0
    def create_matrix(self,x,y):
        for i in range(x):
            self.matrix[i] = {}
            for j in range(y):
                self.matrix[i][j] = Block(i+1,j+1)
    def block(self,i,j):
        for x in self.matrix:
            for y in self.matrix[x].values():
                if y.i == i and y.j == j :
                    return y
        else:
            return None
    def display(self):
        for x in self.matrix:
            for y in self.matrix[x].values():
                    y.plant.printval()
            print()
    def seed(self):
        for x in self.matrix:
            for y in self.matrix[x].values():
                y.plant.reproduce(self)
    def seed2(self): 
        self.two_plants = 0
        self.four_plants = 0
        for x in self.matrix:
            for y in self.matrix[x].values():
                t = y.select_seed()
                if t == '2':
                    self.two_plants += 1
                elif t == '4':
                    self.four_plants += 1
    def perc(self):
        if self.two_plants+self.four_plants :
            print(white + f"\nPercentage of plants : \nTwo seed plants = {100 * self.two_plants/(self.two_plants + self.four_plants)}\nFour seed plants = {100 * self.four_plants/(self.two_plants + self.four_plants)}")
    def run(self):
        self.seed()
        self.seed2()
        self.display()




class Block():
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.plant = No_Plant(self.i,self.j)
        self.seeds = []
        self.parasites = []
    def select_seed(self):
        if self.plant.val == 'X' :
            self.plant.lifetime += 1
            for x in self.seeds:
                del x
            self.seeds = []
            return self.plant.val
        if self.seeds:
            if random.randint(0,50)>len(self.seeds):
                self.plant = self.seeds[random.randint(0,len(self.seeds)-1)]
                self.plant.i,self.plant.j = self.i,self.j
            else:
                self.plant = No_Plant(self.i,self.j)

            #self.plant = self.seeds[random.randint(0,len(self.seeds)-1)]
            #self.plant.i,self.plant.j = self.i,self.j

            for x in self.seeds:
                del x
            self.seeds = []
        else:
            self.plant = No_Plant(self.i,self.j)
        return self.plant.val
    
    def place(self,plant_type):
        if plant_type == 2:
            self.plant = Two_Plant(self.i,self.j)
        elif plant_type == 4:
            self.plant = Four_Plant(self.i,self.j)
        elif plant_type == 0:
            self.plant = No_Plant(self.i,self.j)
        elif plant_type == 'X':
            self.plant = Parasite_plant(self.i,self.j)


class No_Plant():
    def __init__(self,i,j):
        self.i,self.j = i,j
        self.val = '0'

    def printval(self):
        print(white + self.val,end="")
        return self.val
        
    def reproduce(self,matrix):
        pass
    
    def copy(self):
        return No_Plant(self.i,self.j)


class Two_Plant():
    def __init__(self,i,j):
        self.i,self.j = i,j
        self.val = '2'
        self.mutation_percentage = 2

    def printval(self):
        print(blue + self.val,end="")
        return self.val
        
    def copy(self):
        return Two_Plant(self.i,self.j)
    
    def reproduce(self,matrix):
        f = random.randint(0,1)
        matrix.block(self.i,self.j).seeds.append(self.copy())
        global mutations_2_to_4
        if f:
            b1 = matrix.block(self.i -1,self.j)
            b2 = matrix.block(self.i + 1, self.j)
            if b1:
                if random.randint(0,99)<self.mutation_percentage :
                    mutations_2_to_4 += 1
                    b1.seeds.append(Four_Plant(self.i,self.j))
                else:
                    b1.seeds.append(self.copy())
            if b2:
                if random.randint(0,99)<self.mutation_percentage :
                    mutations_2_to_4 += 1
                    b2.seeds.append(Four_Plant(self.i,self.j))
                else:
                    b2.seeds.append(self.copy())
        else:
            b1 = matrix.block(self.i ,self.j - 1)
            b2 = matrix.block(self.i , self.j + 1)
            if b1:
                if random.randint(0,99)<self.mutation_percentage :
                    mutations_2_to_4 += 1
                    b1.seeds.append(Four_Plant(self.i,self.j))
                else:
                    b1.seeds.append(self.copy())
            if b2:
                if random.randint(0,99)<self.mutation_percentage :
                    mutations_2_to_4 += 1
                    b2.seeds.append(Four_Plant(self.i,self.j))
                else:
                    b2.seeds.append(self.copy())

class Four_Plant():
    def __init__(self,i,j):
        self.i,self.j = i,j
        self.val = '4'
        self.mutation_percentage = 5
        
    def printval(self):
        print(red + self.val,end="")
        return self.val
        
    def copy(self):
        return Four_Plant(self.i,self.j)
    
    def reproduce(self,matrix):
        global mutations_4_to_2 
        l = [matrix.block(self.i,self.j),matrix.block(self.i -1,self.j),matrix.block(self.i + 1, self.j),matrix.block(self.i ,self.j - 1),matrix.block(self.i , self.j + 1)]
        for x in l:
            if x:
                if random.randint(0,99) < self.mutation_percentage:
                    x.seeds.append(Two_Plant(self.i,self.j))
                    mutations_4_to_2 += 1
                else:
                    x.seeds.append(self.copy())


class Parasite_plant():
    def __init__(self,i,j):
        self.i,self.j = i,j
        self.val = 'X'
        self.four_take_percentage = 20
        self.two_take_percentage = 20
        self.lifetime = 0   
        self.lifespan = 3

    def printval(self):
        print(green + self.val,end="")
    
    def reproduce(self,matrix):
        l = [matrix.block(self.i,self.j),matrix.block(self.i -1,self.j),matrix.block(self.i + 1, self.j),matrix.block(self.i ,self.j - 1),matrix.block(self.i , self.j + 1)]
        for x in l:
            if x:
                if x.plant.val == '4':
                    if random.randint(0,99) < self.four_take_percentage :
                        x.plant = Parasite_plant(x.i,x.j)
                elif x.plant.val == '2':
                    if random.randint(0,99) < self.two_take_percentage :
                        x.plant = Parasite_plant(x.i,x.j)
        if self.lifetime >= self.lifespan :
            matrix.block(self.i,self.j).plant = No_Plant(self.i,self.j)


mutations_4_to_2 = 0
mutations_2_to_4 = 0
a = Matrix()
a.create_matrix(30,120)

a.block(22,53).place(4)
a.block(3,2).place(2)
a.block(30,48).place(2)
a.block(5,7).place(4)
a.block(5,8).place('X')
a.block(2,118).place(2)
a.block(4,117).place(2)
a.block(7,120).place(2)



'''
for i in range(1,31):
    for j in range(1,121):
        a.block(i,j).place(2)
'''


a.display()
a.perc()
print(white + f"No of 4 to 2 mutations: {mutations_4_to_2}")
print(white + f"No of 2 to 4 mutations: {mutations_2_to_4}")
i = input()

while True:
    a.run()
    a.perc()
    print(white + f"No of 4 to 2 mutations: {mutations_4_to_2}")
    print(white + f"No of 2 to 4 mutations: {mutations_2_to_4}")
    i = input()
