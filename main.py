import pygame, sys, random, math

#
pygame.init()
pygame.display.set_caption('Path Finding Algorithm')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
size = width, height = 800,800
screen = pygame.display.set_mode(size)

#Lever variables
Tiles = []
XPos = 0
YPos = 0
RowCounter = 0
Row1Start = 0
Row2Start = 7
Row3Start = 15
Row4Start = 23
Row5Start = 31
Row6Start = 39
Row7Start = 47
Row8Start = 55
End = 63
Neighbours = []
Marker = 0




#Class declarations
class CTiles:
    XPos, YPos, Width, Height, Row, Column, Path, Mark, Marked = 0, 0, 100, 100, 0, 0, False, 0, False

    def draw_self(self):
        pygame.draw.rect(screen, pygame.Color(random.randint(0,255),50,50), (self.XPos, self.YPos, self.Width, self.Height))

    def __init__(self, Row, Column):
        self.Row = Row
        self.Column = Column

class Entity:
    XPos, YPos, Radius = 0, 0, 0

    def draw_self(self):
        pygame.draw.circle(screen, pygame.Color(255, 255, 0), (self.XPos,self.YPos), self.Radius)

    def __init__(self, Radius, X, Y):
        self.Radius = Radius
        self.XPos = X
        self.YPos = Y




for x in range(8):
    for y in range(8):
        Tiles.append(CTiles(x,y))



while RowCounter >= Row1Start and RowCounter <=Row2Start:
        Tiles[RowCounter].XPos = XPos
        Tiles[RowCounter].YPos = 0
        XPos += 100
        RowCounter += 1
XPos = 0

while RowCounter >= Row2Start and RowCounter <= Row3Start:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 100
    XPos += 100
    RowCounter += 1
XPos = 0

while RowCounter >= Row3Start and RowCounter <= Row4Start:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 200
    XPos += 100
    RowCounter += 1
XPos = 0

while RowCounter >= Row4Start and RowCounter <= Row5Start:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 300
    XPos += 100
    RowCounter += 1
XPos = 0

while RowCounter >= Row5Start and RowCounter <= Row6Start:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 400
    XPos += 100
    RowCounter += 1
XPos = 0

while RowCounter >= Row6Start and RowCounter <= Row7Start:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 500
    XPos += 100
    RowCounter += 1
XPos = 0

while RowCounter >= Row7Start and RowCounter <= Row8Start:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 600
    XPos += 100
    RowCounter += 1
XPos = 0

while RowCounter >= Row8Start and RowCounter <= End:
    Tiles[RowCounter].XPos = XPos
    Tiles[RowCounter].YPos = 700
    XPos += 100
    RowCounter += 1
XPos = 0


#Lever function declarations
def get_tile(x,y):
    if(x == 0):
        return (math.floor(y/100) * 8) + math.ceil(x/100)
    else:
        return (math.floor(y/100) * 8) + math.ceil(x/100) - 1

def find_neighbours(x):
    z = x + 1
    Neighbours = []
    # for i in range(4):
    #     if (i == 0):
    #         Neighbours.append(get_tile(Tiles[x].XPos - 100, Tiles[x].YPos))
    #     elif( i == 1):
    #         Neighbours.append(get_tile(Tiles[x].XPos, Tiles[x].YPos - 100))
    #     elif( i == 2):
    #         Neighbours.append(get_tile(Tiles[x].XPos + 100, Tiles[x].YPos))
    #     else:
    #         Neighbours.append(get_tile(Tiles[x].XPos, Tiles[x].YPos + 100))

    for i in range(4):
        if (i == 0):
            Neighbours.append(get_tile(Tiles[z].XPos - 100, Tiles[z].YPos))
        elif( i == 1):
            Neighbours.append(get_tile(Tiles[z].XPos, Tiles[z].YPos - 100))
        elif( i == 2):
            Neighbours.append(get_tile(Tiles[z].XPos + 100, Tiles[z].YPos))
        else:
            Neighbours.append(get_tile(Tiles[z].XPos, Tiles[z].YPos + 100))

    #Neighbours = [5, -2, 7, 14]
    n = 0
    for _ in range(len(Neighbours)):
        if (Neighbours[n] <= 0 or Neighbours[n] > 64):
            del Neighbours[n]
        else:
            n += 1

    return Neighbours

    # for n in range(4):
    #     if(Neighbours[n - 1] < 0 or Neighbours[n - 1] > 64):
    #         del Neighbours[n - 1]
    #
    # return Neighbours

def find_neighbouring_paths(x):
    Neighbours = find_neighbours(x)
    n = 0
    if Tiles[x].Path == False:
        print('Please choose a valid tile')
    else:
        for _ in range(len(Neighbours)):
            if( Tiles[Neighbours[n]].Path == False):
                del Neighbours[n]
            else:
                n += 1
        return Neighbours

def find_unmarked_neighbouring_paths(x):
    Neighbours = find_neighbouring_paths(x)
    n = 0
    if Tiles[x].Path == False:
        print('Please choose a valid tile')
    else:
        for _ in range(len(Neighbours)):
            if (Tiles[Neighbours[n]].Marked == True):
                del Neighbours[n]
            else:
                n += 1
        return Neighbours



def find_path(x):
    Tiles[x].Marked = True
    Ns = find_unmarked_neighbouring_paths(x)
    return Ns


Tiles[5].Path = True
Tiles[9].Path = True
Tiles[10].Path = True
Tiles[11].Path = True
Tiles[12].Path = True
Tiles[13].Path = True
Tiles[14].Path = True
Tiles[17].Path = True
Tiles[22].Path = True
Tiles[25].Path = True
Tiles[27].Path = True
Tiles[29].Path = True
Tiles[30].Path = True
Tiles[33].Path = True
Tiles[35].Path = True
Tiles[38].Path = True
Tiles[41].Path = True
Tiles[43].Path = True
Tiles[45].Path = True
Tiles[46].Path = True
Tiles[49].Path = True
Tiles[50].Path = True
Tiles[51].Path = True
Tiles[52].Path = True
Tiles[53].Path = True
Tiles[54].Path = True

# print(Tiles[63].Path)

screen.fill(pygame.Color(255,255,255))
for x in range(64):
    if(Tiles[x].Path == False):
        Tiles[x].draw_self()

Entity = Entity(50, 350, 350)
Entity.draw_self()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(find_path((get_tile(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))))

    pygame.display.flip()
