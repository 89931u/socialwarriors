import json
import os
import jsonpatch

__game_config = json.load(open("./config/get_game_config.php_29august2012_nohash.txt", 'r'))

def patch_game_config():
    patch_dir = "./config/patch"
    for patch_file in os.listdir(patch_dir):
        if patch_file.endswith(".patch"):
            f = os.path.join(patch_dir, patch_file)
            patch = json.load(open(f, 'r'))
            jsonpatch.apply_patch(__game_config, patch, in_place=True)
            print(" * Patch applied:", patch_file)

def get_game_config() -> dict:
    return __game_config

def game_config() -> dict:
    return get_game_config()

##########
# PLAYER #
##########

def get_xp_from_level(level: int) -> int:
    return __game_config["levels"][int(level)]["exp_required"]

def get_level_from_xp(xp: int) -> int:
    i = 0
    for lvl in __game_config["levels"]:
        if lvl["exp_required"] > int(xp):
            return i
        i += 1
    return 0

#########
# ITEMS #
#########

items_dict_id_to_items_index = {int(item["id"]): i for i, item in enumerate(__game_config["items"])}

def get_item_from_id(id: int) -> dict:
    items_index = items_dict_id_to_items_index[int(id)] if int(id) in items_dict_id_to_items_index else None
    return __game_config["items"][items_index] if items_index is not None else None

def get_attribute_from_item_id(id: int, attribute_name: str) -> str:
    item = get_item_from_id(id)
    return item[attribute_name] if item and attribute_name in item else None

def get_name_from_item_id(id: int) -> str:
    return get_attribute_from_item_id(id, "name")

############
# MISSIONS #
############

# missions_dict_id_to_missions_index = {int(item["id"]): i for i, item in enumerate(__game_config["missions"])}
# missions_dict_id_to_missions_index = {}

# def get_mission_from_id(id: int) -> dict:
#     items_index = missions_dict_id_to_missions_index[int(id)] if int(id) in missions_dict_id_to_missions_index else None
#     return __game_config["missions"][items_index] if items_index is not None else None
# 
# def get_attribute_from_mission_id(id: int, attribute_name: str) -> str:
#     mission = get_mission_from_id(id)
#     return mission[attribute_name] if mission and attribute_name in mission else None