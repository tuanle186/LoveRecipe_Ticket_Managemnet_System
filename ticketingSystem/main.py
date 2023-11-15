import os
os.system("cls")
print("Đang khởi động...")
from features import autoTransac
from features import manualTransac
from features import printInfo


def main():
    os.system("cls")
    print("-" * 16, "CHỌN MỘT CHỨC NĂNG", "-" * 16)
    print("\n- 1: XỬ LÝ TỰ ĐỘNG\n\n- 2: XỬ LÝ THỦ CÔNG\n\n- 3: KIỂM TRA THÔNG TIN")
    op = int(input("\nLựa chọn: "))
    os.system("cls")
    if op == 1:        
        autoTransac.autoTrsc()
    elif op == 2:
        manualTransac.manualTrsc()
    elif op == 3:
        printInfo.printInfo()
    print()
    os.system("pause")

while True:
    main()