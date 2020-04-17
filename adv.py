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
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

n,e,w,s = 'n','e','w','s'
bt = {n:s,s:n,e:w,w:e}
traversal_path = []
visited = {}
walk_balk = []

#init visited
visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) <  len(room_graph):


    if player.current_room.id not in visited: #enter new room
        visited[player.current_room.id] = player.current_room.get_exits() #add new room to visited w/ possible moves
        visited[player.current_room.id].remove(walk_balk[-1])

    if len(visited[player.current_room.id]) == 0: #hit dead end
        prev_dir = walk_balk.pop()
        player.travel(prev_dir)
        traversal_path.append(prev_dir)

    else: #
        direction = visited[player.current_room.id][-1]


        visited[player.current_room.id].pop()
        traversal_path.append(direction)
        walk_balk.append(bt[direction])
        player.travel(direction)
    print(f'path: {traversal_path} \nvisited: {visited} \nwalkbalk: {walk_balk} \n\n')



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
