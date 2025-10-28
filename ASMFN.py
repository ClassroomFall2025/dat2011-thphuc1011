from quanlinvFN import *
ql = QuanLiNV()
menu = """
1. Nhập danh sách nhân viên
2. Đọc thông tin nhân viên
3. Tìm nhân viên theo mã
4. Xóa thông tin nhân viên
5. Cập nhật thông tin nhân viên
6. Tìm nhân viên theo khoảng lương
7. Sắp xếp thông tin nhân viên từ A-Z
8. Sắp xếp nhân viên theo thu nhập
9. Xuất 5 nhân viên có lương cao nhất"""
while True:
    print(menu)
    lua_chon = input("Nhập lựa chọn 1-9 (0 Để thoát): ")
    match lua_chon:
        case "0":
            print("Thoát chương trình")
            break
        case "1":
            ql.nhap_dsnv()
            ql.luu_dsnv()
        case "2":
            ql.doc_dsnv()
            ql.xuat_dsnv()
        case "3":
            ql.tim_nhan_vien_theo_ma()
        case "4":
            ql.xoa_nhan_vien()
        case "5":
            ql.cap_nhat_thong_tin_nhan_vien()
        case "6":
            ql.tim_nhan_vien_theo_khoang_luong()
        case "7":
            ql.sap_xep_theo_ho_ten()
        case "8":
            ql.sap_xep_theo_thu_nhap()
        case "9":
            ql.xuat_5_nhan_vien_thu_nhap_cao_nhat()
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
