import math

# Hàm tính chu vi và diện tích hình tròn
def Tinh(R):
    # Kiểm tra tính hợp lệ của bán kính
    if R < 0:
        return "Bán kính không hợp lệ. Vui lòng nhập giá trị lớn hơn hoặc bằng 0."
    else:
        # Tính chu vi
        chu_vi = 2 * math.pi * R
        # Tính diện tích
        dien_tich = math.pi * (R ** 2)
        # Kết quả
        return f"Chu vi: {chu_vi:.2f}, Diện tích: {dien_tich:.2f}"

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    # Gọi hàm và in kết quả
    print(Tinh(R))
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
