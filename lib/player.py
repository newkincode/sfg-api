from enum import Enum, auto
import math
from typing import Dict, Union
import pygame
import random

from lib.Object import Object
from lib.plants import plants_list
from lib.farm import tile_map, Tiles
from lib.items import Items


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    STOP = auto()
    UP_LEFT = auto()
    UP_RIGHT = auto()
    DOWN_LEFT = auto()
    DOWN_RIGHT = auto()


class Player(Object):
    speed: float = 3
    inventory: Dict[str, int] = {}
    handle_item: Union[plants_list.plants_type, Items] = Items.NONE

    def __init__(self, image: pygame.Surface, pos: pygame.math.Vector2, screen: pygame.Surface, window_size) -> None:
        super().__init__(image, pos, screen)
        self.window_size = window_size

        # init inventory
        for plant in plants_list.plants_list:
            self.inventory[f"{plant.name}"] = 10
            self.inventory[f"{plant.name}_seed"] = 10
        self.inventory["VITAMIN"] = 10
        self.inventory["gold"] = 0

    def move(self, direction: Direction, frame):
        match direction:
            case Direction.LEFT:
                self.pos.x += -self.speed+frame
            case Direction.RIGHT:
                self.pos.x += self.speed+frame
            case Direction.UP:
                self.pos.y += -self.speed+frame
            case Direction.DOWN:
                self.pos.y += self.speed+frame
            case Direction.UP_LEFT:
                self.pos.x += -self.speed+frame
                self.pos.y += -self.speed+frame
            case Direction.UP_RIGHT:
                self.pos.x += self.speed+frame
                self.pos.y += -self.speed+frame
            case Direction.DOWN_LEFT:
                self.pos.x += -self.speed+frame
                self.pos.y += self.speed+frame
            case Direction.DOWN_RIGHT:
                self.pos.x += self.speed+frame
                self.pos.y += self.speed+frame

        if self.pos.x >= self.window_size[0]-32:
            self.pos.x = self.window_size[0]-33
        if self.pos.x <= 0:
            self.pos.x = 1
        if self.pos.y >= self.window_size[1]-32:
            self.pos.y = self.window_size[1]-32
        if self.pos.y <= 1:
            self.pos.y = 1

    def get_tile_pos(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(
            math.trunc(self.pos.x/32),
            math.trunc(self.pos.y/32)
        )

    def farm_plant(self):
        tPos = self.get_tile_pos()
        tile = tile_map[int(tPos.x)][int(tPos.y)]
        if isinstance(tile, plants_list.plants_list):  # type: ignore
            if tile.maxAge == tile.age:  # type: ignore
                self.inventory[tile.name] += random.randint(0, 4)
                self.inventory[f"{tile.name}_seed"] += 1
                tile_map[int(tPos.x)][int(tPos.y)] = Tiles.FARMLAND

    def plant_plant(self, screen: pygame.Surface) -> bool:
        tPos = self.get_tile_pos()

        # check self
        if not self.handle_item in plants_list.plants_list:
            return False
        if self.inventory[f"{self.handle_item.name}_seed"] == 0:
            return False

        # check farm empty
        if not tile_map[int(tPos.x)][int(tPos.y)] == Tiles.FARMLAND:
            return False

        self.inventory[f"{self.handle_item.name}_seed"] += -1
        tile_map[int(tPos.x)][int(tPos.y)] = self.handle_item(
            tilePosToPos(tPos), screen)  # type: ignore
        return True


def tilePosToPos(tilePos: pygame.math.Vector2) -> pygame.math.Vector2:
    return pygame.math.Vector2(tilePos[0]*32, tilePos[1]*32)
