# Room booking system, 3 buildings, 15 floors / building, 20 room / floor

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Book a room, switch to user input system

rooms[2][11][3] = True

# Check for vacancy on previous building and floor:
vacancy = 0
 
for room_number in range(20):
    if not rooms[2][11][room_number]:
        vacancy += 1
print(vacancy)

# Release a room, switch to user input system

rooms[2][11][3] = False

vacancy = 0
 
for room_number in range(20):
    if not rooms[2][11][room_number]:
        vacancy += 1
print(vacancy)

