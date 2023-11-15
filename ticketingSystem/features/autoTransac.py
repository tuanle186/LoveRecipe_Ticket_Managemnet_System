from modules import transaction as trsc
from modules import worksheet as wks
import pickle
import os


def autoTrsc():
    wks.load_all_values()
    os.system("cls")
    print("-" * 16, "XỬ LÝ TỰ ĐỘNG", "-" * 16)
    
    ###################################### VERIFY TRANSACTION ######################################
    ################################################################################################
    transac = trsc.input_trsc()
    phone_trsc = transac[0]
    std_trsc = transac[1]
    prm_trsc = transac[2]
    money_trsc = transac[3]
    id = f'{phone_trsc}_{std_trsc}_{prm_trsc}'

    rows_id = wks.row_indexes_of(id)
    if len(rows_id) >= 1:
        row = rows_id[0] # Nếu có nhiều ID trùng, thì ID nào tới trước lấy trước
    else:
        return wks.id_not_found(phone_trsc)
        
    wks.print_form(row)

    money_form = wks.get_std_form(row)*130000 + wks.get_prm_form(row)*150000
    valid_money = trsc.print_money_result(money_form, money_trsc) # Kiểm tra xem số tiền có đúng không

    if not valid_money:
        return None
    
    email = wks.get_email(row)
    name = wks.get_name(row)
    phone = phone_trsc
    std = std_trsc
    prm = prm_trsc

    ########################################## BOOK SEATS ##########################################
    ################################################################################################
    from modules import seat_class as seat

    with open('C:/Programming/ticketingSystem/data/layout.pkl', 'rb') as file:
        layout = pickle.load(file)
    
    zoneA, zoneB, zoneC = layout.get_zoneA(), layout.get_zoneB(), layout.get_zoneC()
    zoneA = seat.Zone(zoneA.get_seat_list(), zoneA.get_count(), zoneA.get_max_size())
    zoneB = seat.Zone(zoneB.get_seat_list(), zoneB.get_count(), zoneB.get_max_size())
    zoneC = seat.Zone(zoneC.get_seat_list(), zoneC.get_count(), zoneC.get_max_size())
    layout = seat.Layout(zoneA, zoneB, zoneC)

    to_be_booked_prm_seats = []
    if prm != 0:
        if prm > zoneA.get_remain():
            print(f"\nSố lượng ghế Premium còn lại ({zoneA.get_remain()}) không đủ để đăng ký ❌")
            return None
        else:
            to_be_booked_prm_seats = zoneA.get_empty_seats(prm) # Tự động gợi ý chỗ ngồi

    to_be_booked_std_seats = []
    if std != 0:
        if std > zoneB.get_remain():
            if std > zoneC.get_remain():
                print(f"\nSố lượng ghế Standard còn lại (Zone B: {zoneB.get_remain()}, Zone C: {zoneC.get_remain()}) không đủ để đăng ký ❌")
                return None
            else:
                to_be_booked_std_seats = zoneC.get_empty_seats(std) # Tự động gợi ý chỗ ngồi
        else:
            to_be_booked_std_seats = zoneB.get_empty_seats(std) # Tự động gợi ý chỗ ngồi

    print('-' * 46)
    print("\n*Các ghế gợi ý:")
    if std != 0:
        for seat in to_be_booked_std_seats:
            seat.print()
    if prm != 0:
        for seat in to_be_booked_prm_seats:
            seat.print()
    
    print("\nBạn có muốn đặt các ghế được gợi ý ở trên không?")
    op = input("Lựa chọn (y/n): ")
    if op.capitalize() == 'Y':
        if std != 0: 
            layout.book_seats(to_be_booked_std_seats, email, name, phone)
        if prm != 0: 
            layout.book_seats(to_be_booked_prm_seats, email, name, phone)
        wks.assign_seats(row, to_be_booked_std_seats, to_be_booked_prm_seats)
        print()
        print('-' * 16, "ĐẶT GHẾ THÀNH CÔNG ✅", '-' * 16)
        if std != 0:
            for seat in to_be_booked_std_seats:
                seat.print()
        if prm != 0:
            for seat in to_be_booked_prm_seats:
                seat.print()
    elif op.capitalize() == 'N':
        seats_num = std + prm
        print("\nHãy lần lượt nhập vào ID của các ghế (ví dụ: E27)")
        to_be_booked_seats = []
        i = 1
        while i <= seats_num:
            id = input(f"Ghế {i}: ")
            seat_obj = layout.get_seat_obj(id)
            if seat_obj.get_is_booked():
                print(f"Lỗi: Ghế {id} đã được đặt rồi ❌")
            else:
                i += 1
                to_be_booked_seats.append(seat_obj)
        print("\nTiến hành đặt ghế và gửi email?")
        op = input("Lựa chọn (y/n): ")
        if op.capitalize() == 'N':
            return None
        layout.book_seats(to_be_booked_seats, email, name, phone)
        wks.assign_seats(row, to_be_booked_seats, [])
        print()
        print('-' * 16, "ĐẶT GHẾ THÀNH CÔNG ✅", '-' * 16)
        for seat in to_be_booked_seats:
            seat.print()
    else:
        exit()

    layout.save_changes()

    ########################################## SEND EMAIL ##########################################
    ################################################################################################
    from modules import sendEmail as em
    em.send_email(email, name, phone, std, prm)
    print("\nĐÃ GỬI EMAIL XÁC NHẬN THANH TOÁN THÀNH CÔNG ✅")