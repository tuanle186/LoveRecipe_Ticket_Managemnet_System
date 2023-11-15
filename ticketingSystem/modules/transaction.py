def input_trsc():
    phone = input("\nNhập vào nội dung chuyển khoản:\n\n- Số điện thoại: ")
    std = int(input("\n- Số vé Standard: "))
    prm = int(input("\n- Số vé Premium:  "))
    money = int(input("\n- Số tiền (VND): "))

    # op = input("\nXác nhận thông tin? (y/n): ").lower()
    # while op != 'y' and op != 'n': 
    #     op = input("Sai ký tự, hãy nhập lại (y/n): ")
    # if op == 'n': 
    #     return input_transac_info()
    
    return phone, std, prm, money


def currency_format(input_money):
    input_money = str(input_money)
    reversed_money = input_money[::-1]
    output_money = ''
    for i in range(0, len(input_money)):
        if i % 3 == 0 and i != 0:
            output_money = output_money + ',' + reversed_money[i]
        else:
            output_money = output_money + reversed_money[i]
    return output_money[::-1] + ' VND'


def print_money_result(expected, got):
    print("\n* Thông tin thanh toán:")
    print("- Số tiền cần thanh toán: ", currency_format(expected))
    print("- Số tiền đã nhận được:   ", currency_format(got))
    
    if expected == got:
        print("\n=> GIAO DỊCH THÀNH CÔNG ✅")
        return True
    elif expected > got:
        print("\n=> GIAO DỊCH LỖI ❌ (Nhận thiếu tiền)")
        print("-" * 44)
        return False
        
    else:
        print("\n=> GIAO DỊCH LỖI ❌ (Nhận dư tiền)")
        print("-" * 44)
        return False