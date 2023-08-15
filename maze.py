import random

wall_square = "\u2588\u2588"
empty_square = "  "

size = 65   #should be 2^x + 1 


H = size
W = size


maze = [[0 for _ in range(W)] for _ in range(H)]



def draw_maze(m0):
    for line in m0:
        for x in line:
            if (x == 1):
                print(wall_square, end="")
            else:
                print(empty_square, end="")
        print()

def add_border(m0):
    m0[0] = [1 for _ in range(len(m0[0]))]
    m0[-1] = [1 for _ in range(len(m0[0]))]
    for i in range(2, len(m0) - 2):
        m0[i][0] = 1
        m0[i][-1] = 1
    m0[1][-1] = 1
    m0[len(m0) - 2][0] = 1


def add_walls(Ax, Ay, Bx, By, m0):
    def add_vertical_wall(Ax, Ay, Bx, By, m0):
        if (abs(Ax - Bx) < 3 and abs(Ay - By) < 3):
            return
        else:
            medium_colum = int((Ax + Bx) / 2)
            hole_row = random.randrange(Ay, By, 2) + 1
            for row in range(Ay, (By + 1)):
                m0[row][medium_colum] = 1
            m0[hole_row][medium_colum] = 0
            add_horizontal_wall_2(Ax, Ay, medium_colum, By, m0)
            add_horizontal_wall_2(medium_colum, Ay, Bx, By, m0)

    def add_horizontal_wall(Ax, Ay, Bx, By, m0):
        if (abs(Ay - By) < 3 and abs(Ax - Bx) < 3):
            return
        else:
            medium_row = int((Ay + By) / 2)
            hole_colum = random.randrange(Ax, Bx, 2) + 1
            for colum in range(Ax, (Bx + 1)):
                m0[medium_row][colum] = 1
            m0[medium_row][hole_colum] = 0
            add_vertical_wall_2(Ax, Ay, Bx, medium_row, m0)
            add_vertical_wall_2(Ax, medium_row, Bx, By, m0)

    def add_vertical_wall_2(Ax, Ay, Bx, By, m0):
        if (abs(Ax - Bx) < 3 and abs(Ay - By) < 3):
            return
        else:
            medium_colum = int((Ax + Bx) / 2)
            hole_row = random.randrange(Ay, By, 2) + 1
            for row in range(Ay, (By + 1)):
                m0[row][medium_colum] = 1
            m0[hole_row][medium_colum] = 0
            add_walls(Ax, Ay, medium_colum, By, m0)
            add_walls(medium_colum, Ay, Bx, By, m0)

    def add_horizontal_wall_2(Ax, Ay, Bx, By, m0):
        if (abs(Ay - By) < 3 and abs(Ax - Bx) < 3):
            return
        else:
            medium_row = int((Ay + By) / 2)
            hole_colum = random.randrange(Ax, Bx, 2) + 1
            for colum in range(Ax, (Bx + 1)):
                m0[medium_row][colum] = 1
            m0[medium_row][hole_colum] = 0
            add_walls(Ax, Ay, Bx, medium_row, m0)
            add_walls(Ax, medium_row, Bx, By, m0)


    if (random.randint(0,1)):
        add_vertical_wall(Ax, Ay, Bx, By, m0)
    else:
        add_horizontal_wall(Ax, Ay, Bx, By, m0)
        




add_walls(0,0,W - 1,H - 1,maze)
add_border(maze)
draw_maze(maze)
