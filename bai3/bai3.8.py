import math

# Hàm chính
def tinh_khoang_cach():
    # Tọa độ ban đầu (0, 0)
    x, y = 0, 0

    # Nhập vào các lệnh di chuyển
    print("Nhập các lệnh di chuyển (dạng: UP 5, DOWN 3,...). Nhấn Enter để kết thúc nhập.")
    while True:
        lenh = input("Nhập lệnh: ")
        if not lenh:  # Dừng khi người dùng không nhập gì
            break
        huong, buoc = lenh.split()
        buoc = int(buoc)

        # Xử lý các hướng di chuyển
        if huong == "UP":
            y += buoc
        elif huong == "DOWN":
            y -= buoc
        elif huong == "LEFT":
            x -= buoc
        elif huong == "RIGHT":
            x += buoc

    # Tính khoảng cách đến gốc tọa độ (0, 0)
    khoang_cach = math.sqrt(x**2 + y**2)

    # Làm tròn đến số nguyên gần nhất
    print(f"Khoảng cách từ vị trí hiện tại đến gốc tọa độ: {round(khoang_cach)}")

# Gọi hàm chính
tinh_khoang_cach()
