import random as rnd

def game_over(cnt):
    if cnt == 1:
        print("Неверно введены параметры")
    if cnt == 2:
        print("Число бомб больше размеров поля")
    if cnt == 3:
        print("Вы проиграли.")
    exit(0)

class Saper:
    def __init__(self, width=5, height=5, cnt_bomb=2):
        self.width = width
        self.height = height
        self.cnt_bomb = cnt_bomb
        self.field = [[0]*width]*height
        self.open_ceils = [[False]*width]*height
        self.flags = [[False]*width]*height
        self.step = [ [-1, -1], [-1, 0],  [-1, 1],  [0, -1], [0, 1],  [1, -1],  [1, 0],  [1, -1] ]
        

        for bomb in range(cnt_bomb):
            x = rnd.randint(0, width-1)
            y = rnd.randint(0, height-1)
            self.field[x][y] = 1
        
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j] != -1:
                    for dx, dy in self.step:
                        if 0 <= i + dx and i + dx < self.width and 0 <= j + dy and j + dy < self.height: 
                            self.field[i][j] += 1 

    def open(self, x, y):
        if self.field[x][y] == -1:
            game_over(3)

        self.open_ceils[x][y] = True
        
        if self.field[x][y] != 0:
            return

        for dx, dy in self.step:
            if self.open_ceils == False and (0 <= x + dx and x + dx < self.width and 0 <= y + dy and y + dy < self.height):
                open(x+dx, y+dy)

                

    def print_field(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.open_ceils:
                    print(self.field[x][y], end=" ")
                else:
                    print(".", end=" ")
            print()

if __name__ == "__main__":

    print('''Выберете режим (введите число)
    1-базовый
    2-средний''')

    try:
        level = input()
    except:
        game_over(1)

    level = int(level) 
    if level == 1:
        sap = Saper(5, 5, rnd.randint(2, 5))

    elif level == 2:
        print("Введите через пробел ширину, высоту поля и количество бомб:")
        try:
            w, h, b = input()
        except:
            game_over(1)
        
        if w * h < b:
            game_over(2)

        sap = Saper(w, h, b)

    else:
        game_over(1)

    while True:
        print("Введите действие")
        try:
            s = input().split()
            x = int(s[0])
            y = int(s[1])
            action = s[2]
        except:
            game_over(1)
        
        if x < 1 or x > sap.width or y < 1 or y > sap.height:
            game_over(1)
        
        x -= 1
        y -= 1
        
        if action == "Flag":
            sap.flags[x][y] = True
        elif action == "Open":
            if sap.field[x][y] == -1:
                game_over(3)
            else:
                sap.open(x, y)
                sap.print_field()

        else:
            game_over(1)
