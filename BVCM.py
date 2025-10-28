from QLBV import *
ql = QuanLiBV()

menu = """
0. Thoát
1. Nhập danh sách hóa đơn
2. Xuất danh sách hóa đơn
3. Xuất danh sách hóa đơn có đánh giá "Cao" về mức sử dụng
4.  Sắp xếp danh sách hóa đơn theo tổng tiền thanh toán"""

while True:
    print("==="*5 + "MENU" + "==="*13)
    print(menu)
    print("==="*5 + "====" + "==="*13)
    lua_chon = input("Nhập lựa chọn của bạn: ")
    match lua_chon:
        case "0":
            print("Kết thúc")
            break
        case "1":
            ql.nhap_DSHD()
        case "2":
            ql.xuat_DSHD()
        case "3":
            ql.xuat_DSHD_DGC()
        case "4":
            ql.sap_xep_DSHD()
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 0-4")