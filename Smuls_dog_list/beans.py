class Dog:

    
    def __init__(self, Ras, Storlek, Färg):
        self.Ras = Ras
        self.Storlek = Storlek
        self.Färg = Färg
    
    def set_Färg(self, Färg):
        self.Färg = Färg
 
    def get_Färg(self):
        return self.Färg

    def get_Storlek(self, Storlek):
        return self.Storlek 

    def get_Ras(self, Ras):
        return self.Ras