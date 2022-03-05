
from random import randint
from .Platforms import Platforms
from .Gate import Gate
from .Constants import Constants

class Gameboard:
    def __init__(self):#инициализация
       
        self.Constants = Constants()
        self.cell_size = self.Constants.cell_size
        
        
        self.grid = self.create_grid()
        
       
        self.Platform = Platforms()
        self.platforms = self.Platform.generate_platforms()

        

    def create_grid(self): #создание игрового поля
       
        grid = []
        for row in range(self.Constants.grid_rows):
            for column in range(self.Constants.grid_columns):
                
                row_coordinate = self.cell_size * (row + 2)
                column_coordinate = self.cell_size * column

                grid.append([column_coordinate, row_coordinate])
       
        return grid
    
    def generate_gate(self, platforms, entry_gate_index=0, exit_gate=False): #генерация ворот входа и выхода
        
        row_index = randint(0, self.Constants.platforms_num - 1)

        
        if exit_gate == True:
            for platform in platforms:                
                while (row_index == entry_gate_index):
                    row_index = randint(0, self.Constants.platforms_num - 1)
                
        else:
            pass


        for platform in platforms:
            x_in_platform = platforms[row_index].x >= platform.x and platforms[row_index].x <= platform.x + platform.width
            y_in_platform = platforms[row_index].y == platform.y
            print(x_in_platform," x ",gate_x,"/",y_in_platform," y ",gate_y)
            print(platforms[row_index].x,"/",platforms[row_index].y)
            if (x_in_platform and y_in_platform):
                row_index-=1
                while (row_index == entry_gate_index):
                    row_index = randint(0, self.Constants.platforms_num - 1)
                
        gate_y = platforms[row_index].y
        
        gate_x = randint((platforms[row_index].x) // self.cell_size + 1,
                         (platforms[row_index].x + platforms[row_index].width)
                         // (self.cell_size) - 1)
        gate_x *= self.cell_size
        for platform in platforms:
            x_in_platform = platform.x == gate_x
            y_in_platform = platform.y == gate_y
            #print(x_in_platform," x ",gate_x,"/",y_in_platform," y ",gate_y)
           # print(platform.x,"/",platform.y)
            
            if (y_in_platform):
                gate_y =gate_y - 0
                
                

        print(row_index)
        print("qopit")
        return Gate(gate_x, gate_y, row_index)
    
    def is_inside_platform(self, x: int, y: int, platforms: list): #проверка на плотформу
        is_inside = False

        for platform in platforms:
            x_in_platform = x >= platform.x and x <= platform.x + platform.width
            y_in_platform = y == platform.y
            if (x_in_platform and y_in_platform):
                is_inside = True

        return is_inside
    

