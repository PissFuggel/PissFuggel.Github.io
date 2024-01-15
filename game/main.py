import character

player =character.Character(0,0,5)


print("Welcome to the burkel bank dungeon")
while True:
    print("Choose where you want to go")
    print("1. NORTH \n2. EAST \n3. SOUTH \n4. WEST ")
    player_input = input()


    match player_input:
        case "1":
            player.change_pos(0, -1)
        case "2":
            player.change_pos(1, 0)
        case "3":
            player.change_pos(0, 1)
        case "4":
            player.change_pos(-1, 0)

    #print(map.get_room(player.x_pos, player.y_pos))