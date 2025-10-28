from quanlisv import *
ql = QuanLiSV()

menu = """
1. Nhập danh sách nhân viên
2. Xuất thông tin danh sách sinh viên
3. Xuất danh sách sinh viên có học lực giỏi
4. Sắp xếp danh sách sinh viên theo điểm
5. Kết thúc"""
while True:
    print("==="*5 + "MENU" + "==="*8)
    print(menu)
    print("==="*5 + "====" + "==="*8)
    lua_chon = input("Nhập lựa chọn của bạn: ")
    match lua_chon:
        case "1":
            ql.nhap_dssv()
        case "2":
            ql.xuat_dssv()
        case "3":
            ql.xuat_dssv_gioi()
        case "4":
            ql.sap_xep_dssv()
        case "5":
            print("Kết thúc")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1-5")