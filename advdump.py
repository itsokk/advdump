# Made by itsokk
# 18/4/2022

import requests
import json

v = input("Version: ")
l = input("Language: ")
r = requests.get(
    f"https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/{v}/assets/minecraft/lang/{l}.json"
).json()
x = {}
for i in r.keys():
    if i.startswith("advancements"):
        if i.endswith("title"):
            x[
                i.replace("advancements.", "").replace(".title", "").replace(".", "/")
            ] = r[i]
with open(f"{v}_{l}.json", "w") as z:
    json.dump(x, z)
