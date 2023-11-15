def printInfo():
    from modules import seat_class as seat
    import pickle
    import os

    os.system("cls")
    with open('C:/Programming/ticketingSystem/data/layout.pkl', 'rb') as file:
        layout = pickle.load(file)
    zoneA, zoneB, zoneC = layout.get_zoneA(), layout.get_zoneB(), layout.get_zoneC()
    zoneA = seat.Zone(zoneA.get_seat_list(), zoneA.get_count(), zoneA.get_max_size())
    zoneB = seat.Zone(zoneB.get_seat_list(), zoneB.get_count(), zoneB.get_max_size())
    zoneC = seat.Zone(zoneC.get_seat_list(), zoneC.get_count(), zoneC.get_max_size())
    layout = seat.Layout(zoneA, zoneB, zoneC)


    def remain_seats():
        print("\n- Zone A:",  zoneA.get_remain(), "/", zoneA.get_max_size())
        print("- Zone B:",  zoneB.get_remain(), "/", zoneB.get_max_size())
        print("- Zone C:",  zoneC.get_remain(), "/", zoneC.get_max_size())


    print("-" * 16, "KIỂM TRA THÔNG TIN", "-" * 16)
    print("\n- 1: Kiểm tra thông tin tất cả các ghế")
    print("\n- 2: Kiểm tra số lượng ghế còn lại")

    op = int(input("\nLựa chọn: "))

    if op == 1:
        layout.print()
    elif op == 2:
        remain_seats()