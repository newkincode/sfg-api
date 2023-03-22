import json
import os
import re
import lib.plants.plants_list as plantsList
import importlib
import glob
import lib.runtime_values as runtime_values


data = os.listdir("mods")
data = [re.sub('.py', '', i) for i in data]
modClassList = []

# 파일 경로를 사용하여 모듈 import
for data in data:
    # importlib를 사용하여 모듈 import
    module = importlib.import_module("." + data, package="mods")
    # import한 모듈 사용 예시
    modClassList.append(module.mod())
for i in modClassList:
    plantsList.plants_list.append(i)