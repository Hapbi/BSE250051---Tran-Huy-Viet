for i in range(1, 4):
    name = input(f"Nhập tên sinh viên {i}: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    
    dtb = (toan + ly + hoa) / 3
    print(f"Sinh viên: {name}, Điểm trung bình: {dtb:.2f}")

