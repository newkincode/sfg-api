import json
import os
import re

data = os.listdir("mods")
data = [re.sub('.py', '', i) for i in data]
modClassList = []

import importlib
import glob

# 불러올 파일들이 있는 폴더 경로
folder_path = "mods"

# 폴더 내 모든 파일 경로 가져오기
file_paths = glob.glob(os.path.join(folder_path, "*.py"))

# 파일 경로를 사용하여 모듈 import
for file_path in file_paths:
    # 파일 경로에서 파일명만 추출
    module_name = os.path.basename(file_path)[:-3] # 파일명에서 .py 확장자 제외
    # importlib를 사용하여 모듈 import
    module = importlib.import_module("." + module_name, package="mods")
    # import한 모듈 사용 예시
    modClassList.append(module.mod())
for i in modClassList:
    i.test()