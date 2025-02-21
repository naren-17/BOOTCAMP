class Robot:
    def __init__(self, energy_level, model):
        self.__energy_level = energy_level
        self._model = model
        
    def get_energy(self):
        return(f"the current energy is: {self.__energy_level}")
    
    def set_energy(self, energy_level):
        if 0 <= energy_level <=100:
            self.__energy_level = energy_level
        else:
            print("energy level should be betweeen 0 and 100")
            
    def charge(self):
        self.__energy_level = 100
        return(f"the new energy level is : {self.__energy_level}")
                
my_robot = Robot(50, 2023)
print(my_robot.get_energy())
print(my_robot.charge())

