import lib.ModClass as modClass
import lib.plants.Plants as plants
import pygame
import random
import lib.runtime_values

class mod(plants.Plants, modClass.ModClass):
    ver = ("test", 1,0,0) # name ver1 ver2 ver3
    name = "rice"  # 영어로 적고 lang 파일에서 참조.
    price = 100
    maxAge = 2
    
    def __init__(self) -> None:
        print(f"{self.ver[0]} {self.ver[1]}.{self.ver[2]}.{self.ver[3]}")
        
        self.growCount = 0
        self.age = 0
        self.watered = False
        self.rotCount = 0
        super().__init__(lib.runtime_values.players[0].pos, lib.runtime_values.screen)

    def grow(self):
        if self.watered:
            self.growCount += random.randint(0, 10)
            if (self.growCount < 10000) and (self.age):
                self.update_image(
                    pygame.image.load(f"assets/img/plants/{self.name}/farm_0.png"))
            if (self.growCount >= 10000) and (self.age == 0):
                self.update_image(
                    pygame.image.load(f"assets/img/plants/{self.name}/farm_1.png"))
                self.age += 1
                self.watered = False
            if (self.growCount >= 25000) and (self.age == 1):
                self.update_image(
                    pygame.image.load(f"assets/img/plants/{self.name}/farm_2.png"))
                self.age += 1
                self.watered = False

    def rot(self):
        if self.rotCount >= 5000:
            return True
        if self.watered == False:
            self.rotCount += random.randint(0, 5)