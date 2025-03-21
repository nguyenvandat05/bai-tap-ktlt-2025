# Định nghĩa hàm benefit
def benefit(t, n, k):
    # Tính lãi suất từ phần trăm sang dạng thập phân
    lai_suat = t / 100
    # Tính số tiền nhận được sau k tháng
    so_tien = n * (1 + lai_suat) ** k
    return so_tien

# Nhập từ bàn phím
try:
    t = float(input("Nhập lãi suất (t%/tháng): "))
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng gửi (k): "))

    # Gọi hàm benefit và in kết quả
    ket_qua = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng: {ket_qua:.2f}")
except ValueError:
    print("Vui lòng nhập dữ liệu hợp lệ!")
