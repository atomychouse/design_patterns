class House:
    
    def __init__(self):
        self.__wall = None
        self.__floor = None
        self.__roof = None
        
    def setWall(self, wall):
        self.__wall = wall
        
    def setFloor(self, floor):
        self.__floor = floor
    
    def setRoof(self, roof):
        self.__roof = roof
        
    def build_house(self):
        print(self.__roof.size  * f'roof {self.__roof.material}')
        print(self.__wall.size  * f'wall {self.__wall.material}\n')
        print(self.__floor.size * f'floor {self.__floor.material}')
        
class Builder:
    def doWall(self): pass
    def doFloor(self): pass
    def doRoof(self): pass
    
class Wall:
    size = None
    material = None
    
    
class Roof:
    weight = None
    material = None

    
class Floor:
    size = None
    material = None
        

class HouseBuilder(Builder):
    def doWall(self):
        wall = Wall()
        wall.size = 20
        wall.material = 'brick'
        return wall
    
    def doFloor(self):
        floor = Floor()
        floor.size = 10
        floor.material = 'wood'
        return floor
    
    def doRoof(self):
        roof = Roof()
        roof.size = 10
        roof.material = 'concreto'
        return roof
    

    
class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
        
        
    def getHouse(self):
        house = House()
        roof = self.__builder.doRoof()
        house.setRoof(roof)
        wall = self.__builder.doWall()
        house.setWall(wall)
        floor = self.__builder.doFloor()
        house.setFloor(floor)
        building = house.build_house()
        return building
        
        

domyhouse = HouseBuilder()
director = Director()
director.setBuilder(domyhouse)
director.getHouse()