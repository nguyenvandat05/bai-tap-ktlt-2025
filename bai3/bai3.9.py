# Hàm thực hiện các phép toán
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Không thể chia cho 0!"

# Chương trình chính
def may_tinh_don_gian():
    print("Chào mừng bạn đến với chương trình tính toán đơn giản!")
    print("Chọn phép tính:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")

    # Nhập lựa chọn từ người dùng
    lua_chon = input("Nhập số của phép tính (1/2/3/4): ")

    if lua_chon in ['1', '2', '3', '4']:
        # Nhập hai số
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))

        # Thực hiện phép tính dựa trên lựa chọn
        if lua_chon == '1':
            print(f"Kết quả: {a} + {b} = {cong(a, b)}")
        elif lua_chon == '2':
            print(f"Kết quả: {a} - {b} = {tru(a, b)}")
        elif lua_chon == '3':
            print(f"Kết quả: {a} * {b} = {nhan(a, b)}")
        elif lua_chon == '4':
            print(f"Kết quả: {a} / {b} = {chia(a, b)}")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

# Gọi chương trình
may_tinh_don_gian()
