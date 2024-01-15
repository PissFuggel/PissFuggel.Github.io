"""
X = inget
M = monster
C = Chest
B = Boss


"""
rooms = (("X","X","C"),
        ("X","M","X"),
        ("M","X","B"))

def get_room(x,y):
    return rooms[y][x]

print(get_room(0,2))
