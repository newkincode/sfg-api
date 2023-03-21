from lib.plants import plants_list
from lib import runtime_values

def sell(plant):
    if runtime_values.players[0].handle_item in plants_list.plants_list:
        if runtime_values.players[0].inventory[f"{plants_list.plants_list[plants_list.plants_list.index(plant)].name}"] > 0:
            runtime_values.players[0].inventory["gold"] += plants_list.plants_list[plants_list.plants_list.index(plant)].price
            runtime_values.players[0].inventory[f"{plants_list.plants_list[plants_list.plants_list.index(plant)].name}"] -= 1
def buy(plant):
    if runtime_values.players[0].handle_item in plants_list.plants_list:
        if runtime_values.players[0].inventory["gold"] > plants_list.plants_list[plants_list.plants_list.index(plant)].price+5:
            runtime_values.players[0].inventory["gold"] -= plants_list.plants_list[plants_list.plants_list.index(plant)].price+5
            runtime_values.players[0].inventory[f"{plants_list.plants_list[plants_list.plants_list.index(plant)].name}"] += 1
    if runtime_values.players[0].handle_item.name == "VITAMIN":
        if runtime_values.players[0].inventory["gold"] > 15:
            runtime_values.players[0].inventory["gold"] -= 15
            runtime_values.players[0].inventory["VITAMIN"] += 1