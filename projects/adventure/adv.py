from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
go_back = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
model = {player.current_room.id: {}}
stack = []
for direction in player.current_room.get_exits():
    move = model[player.current_room.id].setdefault(direction, '?')
    if move == '?':
        stack.append(direction)

while stack:
    move_direction = stack.pop()
    traversal_path.append(move_direction)
    prev_room = player.current_room
    player.travel(move_direction)
    model[prev_room.id][move_direction] = player.current_room.id
    model.setdefault(player.current_room.id, {})
    model[player.current_room.id][go_back[move_direction]] = prev_room.id
    for direction in player.current_room.get_exits():
        move = model[player.current_room.id].setdefault(direction, '?')
        if move == '?':
            stack.append(direction)
    if '?' in model[player.current_room.id].values():
        continue
    else:
        r = -1
        while player.current_room.id != 0 and '?' in model[0].values():
            print(f'True')
            move_direction = go_back[traversal_path[r]]
            traversal_path.append(move_direction)
            player.travel(move_direction)
            r -= 2
            if '?' in model[player.current_room.id].values():
                break
print(model)



# add unexplored exits to stack of directions from this location to be searched
# mark this room as having been catalogued ??
# pop a direction and travel, adding direction to traversal_path
# repeat
# if all directions from a room have been traveled, unwind path until room found with unexplored directions




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
