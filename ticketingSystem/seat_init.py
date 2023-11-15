from modules import seat_class_adjust as seat_class
import pickle

zoneA, zoneB, zoneC = [], [], []
for char in ('E', 'F', 'G', 'H', 'J', 'K'):
    if char == 'F' or char == 'H' or char == 'K':
        for num in range(6, 28):
            seatID = char + str(num)
            zoneA.append(seat_class.Seat(seatID, True))
    else:
        for num in range(27, 5, -1):
            seatID = char + str(num)
            zoneA.append(seat_class.Seat(seatID, True))

for char in ('L', 'M', 'N', 'P', 'Q', 'R'):
    if char == 'M' or char == 'P' or char == 'R':
        for num in range(1, 23):
            seatID = char + str(num)
            zoneB.append(seat_class.Seat(seatID, False))
    else:
        for num in range(22, 0, -1):
            seatID = char + str(num)
            zoneB.append(seat_class.Seat(seatID, False))

for char in ('E', 'F', 'G', 'H', 'J', 'K'):
    if char == 'F' or char == 'H' or char == 'K':
        for num in range(1 , 6):
            seatID = char + str(num)
            zoneC.append(seat_class.Seat(seatID, False))
    else:
        for num in range(5, 0, -1):
            seatID = char + str(num)
            zoneC.append(seat_class.Seat(seatID, False))

zoneA = seat_class.Zone(zoneA, 0, len(zoneA))
zoneB = seat_class.Zone(zoneB, 0, len(zoneB))
zoneC = seat_class.Zone(zoneC, 0, len(zoneC))
layout = seat_class.Layout(zoneA, zoneB, zoneC)

# with open('C:/Programming/ticketingSystem/data/layout1.pkl', 'wb') as file:
#     pickle.dump(layout, file)


layout.print()