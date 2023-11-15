def manualTrsc():
    from modules import seat_class as seat
    import pickle
    import os
    from modules import sendEmail as em
    os.system("cls")

    with open('C:/Programming/ticketingSystem/data/layout.pkl', 'rb') as file:
        layout = pickle.load(file)

    zoneA, zoneB, zoneC = layout.get_zoneA(), layout.get_zoneB(), layout.get_zoneC()
    zoneA = seat.Zone(zoneA.get_seat_list(), zoneA.get_count(), zoneA.get_max_size())
    zoneB = seat.Zone(zoneB.get_seat_list(), zoneB.get_count(), zoneB.get_max_size())
    zoneC = seat.Zone(zoneC.get_seat_list(), zoneC.get_count(), zoneC.get_max_size())
    layout = seat.Layout(zoneA, zoneB, zoneC)


    def book_seats():
        print()
        print("-" * 46)
        seats_num = int(input("\nSố lượng ghế muốn đặt: "))
        print("\nHãy lần lượt nhập vào ID của các ghế (ví dụ: E27)")
        to_be_booked_seats = []
        for i in range(1, seats_num + 1):
            id = input(f"Ghế {i}: ")
            seat_obj = layout.get_seat_obj(id)
            if seat_obj.get_is_booked():
                print(f"Lỗi: Ghế {id} đã được đặt rồi ❌")
                exit()
            to_be_booked_seats.append(seat_obj)
        email = input("\nEmail: ")
        name = input("Họ và tên: ")
        phone = input("Số điện thoại: ")
        layout.book_seats(to_be_booked_seats, email, name, phone)
        print("\nĐặt ghế thành công ✅")


    def clear_seats():
        print()
        print("-" * 46)
        delSeats_num = int(input("\nSố lượng ghế muốn hủy: "))
        print("\nHãy lần lượt nhập vào ID của các ghế (ví dụ: E27)")
        to_be_cleared_seats = []
        for i in range(1, delSeats_num + 1):
            id = input(f"Ghế {i}: ")
            delSeat_obj = layout.get_seat_obj(id)
            to_be_cleared_seats.append(delSeat_obj)
        layout.clear_seats(to_be_cleared_seats)
        print("\nHủy đặt ghế thành công ✅")


    def send_email():
        print()
        print("-" * 46)
        email = input("\n- Email: ")
        name = input("- Họ và tên: ")
        phone = input("- Số điện thoại: ")
        std = int(input("- Số vé Standard: "))
        prm = int(input("- Số vé Premium: "))
        op = input("\nXác nhận gửi mail? (y/n): ")
        if op.capitalize() == 'N':
            return None
        em.send_email(email, name, phone, std, prm)
        
        print("\nĐÃ GỬI MAIL THÀNH CÔNG ✅")


    print("-" * 16, "XỬ LÝ THỦ CÔNG", "-" * 16)
    print("\n- 1: Đặt chỗ\n\n- 2: Hủy đặt chỗ\n\n- 3: Gửi email xác nhận")
    op = int(input("\nLựa chọn: "))

    if op == 1:
        book_seats()
    elif op == 2:
        clear_seats()
    elif op == 3:
        send_email()
        
    layout.save_changes()