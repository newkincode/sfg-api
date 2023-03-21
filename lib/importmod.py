import json
import os
import re

data = os.listdir("mods")
data = [re.sub('.py', '', i) for i in data]

with open("data/modlist.json", 'w', encoding='utf-8') as file:
    json.dump(data, file)