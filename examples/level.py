# This example helps you level your mining, woodcutting, and player level, and it changes which resource is farmed depending on the player level
# This example relies on the package to be installed. Please install it using pip install --upgrade artifactsmmo-wrapper
token = "YOUR_TOKEN_HERE" # TODO: Make sure to paste your token here
doods = ["YOUR_CHARACTERS_HERE"] # TODO: Make sure to fill in your characters into this array. If you have 1, or if you have 5, make sure to put them here

import threading
from artifactsmmo_wrapper import ArtifactsAPI
from itertools import cycle

def deposit(api):
    items = ""
    golds = 0
    api.actions.move(*api.content_maps.bank)
    for item in api.char.inventory:
        items += f"{item.quantity}x {item.code}, "
        api.actions.bank_deposit_item(item.code, item.quantity)
    
    if api.char.gold > 0:
        golds = api.char.gold
        api.actions.bank_deposit_gold(api.char.gold)
    
    items = items.strip().strip(",")
    d = "Deposited"
    if items:
        d += items
    
    if golds:
        d += str(golds)
        
    if d == "Deposited":
        d += " nothing"
    api._print(d)


def mining(api, stop):
    if api.char.mining_level < api.content_maps.mithril_rocks.level:
        if api.char.mining_level < api.content_maps.gold_rocks.level:
            if api.char.mining_level < api.content_maps.coal_rocks.level:
                if api.char.mining_level < api.content_maps.iron_rocks.level:
                    content_map = api.content_maps.copper_rocks
                else:
                    content_map = api.content_maps.iron_rocks
            else:
                content_map = api.content_maps.coal_rocks
        else:
            content_map = api.content_maps.gold_rocks
    else:
        content_map = api.content_maps.mithril_rocks
        
    api._print(f"Mining {content_map.name}")
    api.actions.move(*content_map)
    while not stop.is_set():
        try:
            if api.char.get_inventory_space() < 5:
                return True  # Return True to indicate we need to deposit
            api.actions.gather()
        except:
            stop.set()
            exit(0)()
            return True
    return False

def woodcutting(api, stop):
    if api.char.mining_level < api.content_maps.maple_tree.level:
        if api.char.mining_level < api.content_maps.birch_tree.level:
            if api.char.mining_level < api.content_maps.spruce_tree.level:
                content_map = api.content_maps.ash_tree
            else:
                content_map = api.content_maps.spruce_tree
        else:
            content_map = api.content_maps.birch_tree
    else:
        content_map = api.content_maps.maple_tree

    api._print(f"Cutting {content_map.name}")
    api.actions.move(*content_map)
    while not stop.is_set():
        try:
            if api.char.get_inventory_space() < 5:
                return True  # Return True to indicate we need to deposit
            api.actions.gather()
        except:
            stop.set()
            exit(0)()
            return True
    return False

def combat(api, stop):
    content_map = api.content_maps.chicken

    api._print(f"Fighting {content_map.name}")
    api.actions.move(*content_map)
    while not stop.is_set():
        try:
            if api.char.get_inventory_space() < (api.char.inventory_max_items / 2):
                return True  # Return True to indicate we need to deposit
            api.actions.fight()
            api.actions.rest()
        except:
            stop.set()
            exit(0)()
            return True
    return False

def task_rotation(api, stop):
    tasks = cycle([combat, woodcutting, mining])
    current_task = next(tasks)
    
    deposit(api)
    
    while not stop.is_set():
        needs_deposit = current_task(api, stop)
        if needs_deposit:
            deposit(api)
            current_task = next(tasks)  # Move to next task after depositing

chars = [ArtifactsAPI(token, dood) for dood in doods]

stop = threading.Event()

threads = []
for api in chars:
    thread = threading.Thread(target=task_rotation, args=[api, stop])
    threads.append(thread)
    try:
        thread.start()
    except KeyboardInterrupt:
        stop.set()


for thread in threads:
    thread.join()