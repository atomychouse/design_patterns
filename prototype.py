import copy 

class Prototype:

    def __init__(self, name , color):
        self.__name = name
        self.__color = color
    
    
    def set_name(self, name):
        self.__name = name
    
    def set_color(self, color):
        self.__color = color
        
    def set_full(self, full):
        self.__name = full['name']
        self.__color = full['color']
    
    def clone(self):
        return copy.copy(self)
        
    def get_robodata(self):
        robosay = f"My name is {self.__name} I am in color {self.__color}"
        return robosay 


robo1 = Prototype(**{'name':'c3p0','color':'gold'})
robo2 = robo1.clone()
robo2.set_name(name ='R2D2')
robo2.set_color(color ='white')
robo3 = robo1.clone()
full = {'name':'BKD2','color':'BLACK'}
robo3.set_full(full)

robots = [robo1.get_robodata(), robo2.get_robodata(), robo3.get_robodata()]

print(robots)