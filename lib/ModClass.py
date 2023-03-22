import pygame

class ModClass:
    ver: tuple[str, int, int, int] # name ver1 ver2 ver3
    
    def __init__(self) -> None:
        print(f"{self.ver[0]} {self.ver[1]}.{self.ver[2]}.{self.ver[3]}")