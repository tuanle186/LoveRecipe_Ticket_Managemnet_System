import gspread
sh = gspread.service_account().open("LoveRecipe_Responses_Ver1.2")
responses = sh.worksheet("Responses")
seat_layout = sh.worksheet("seat_layout")


def load_all_values():
    global matrix 
    matrix = responses.get_all_values()


def row_indexes_of(key): # Key can either be ID or Phone Num
    row_indexes = []
    if '_' in key:
        for i in range(1, responses.row_count):
            if matrix[i][6] == 'TRUE':
                continue
            row_ID = f'{matrix[i][3]}_{matrix[i][4]}_{matrix[i][5]}'
            if row_ID == key:
                row_indexes.append(i)
    else:
        for i in range(1, responses.row_count):
            if matrix[i][6] == 'TRUE':
                continue
            phone = matrix[i][3]
            if phone == key:
                row_indexes.append(i)
    return row_indexes


def get_email(row):
    return matrix[row][1]


def get_name(row):
    return matrix[row][2]


def get_phone(row):
    return matrix[row][3]


def get_std_form(row):
    return int(matrix[row][4])


def get_prm_form(row):
    return int(matrix[row][5])


def succesfully_processed(row):
    responses.update_cell(row + 1, 9, 'TRUE')


def assign_seats(row, std_list, prm_list):
    seat_str = ''
    if len(std_list) != 0:
        for seat in std_list:
            if len(seat_str) != 0:
                seat_str += ', ' + str(seat.get_id())
            else:
                seat_str += str(seat.get_id())
    
    if len(prm_list) != 0:
        for seat in prm_list:
            if len(seat_str) != 0:
                seat_str += ', ' + str(seat.get_id())
            else:
                seat_str += str(seat.get_id())
    
    range = f'I{row + 1}:J{row + 1}'
    responses.update(range, [[True, seat_str]])


def id_not_found(phone):
    row_indexes = row_indexes_of(phone)
    if len(row_indexes) == 0:
        print("\nLỖI: Không tìm thấy số điện thoại đăng ký ❌")
    else:
        print_form(row_indexes[0])
        print(f"\nLỖI: Tìm thấy {len(row_indexes)} SĐT đăng ký nhưng số vé không trùng khớp ❌")
    return None
        

def print_form(row):
    print("\n------------ CHI TIẾT GIAO DỊCH ------------")
    print("- Email:", get_email(row))
    print("- Họ và tên:", get_name(row))
    print("- Số điện thoại:", get_phone(row))
    print("- Số vé Standard đăng ký:", get_std_form(row))
    print("- Số vé Premium đăng ký:", get_prm_form(row))
