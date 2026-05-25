# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input:

# ho_ten (String): Cần xử lý loại bỏ khoảng trắng dư thừa ở hai đầu.

# tuoi (Integer): Cần ép kiểu từ dữ liệu nhập vào và kiểm tra phạm vi.

# Output:

# Trường hợp hợp lệ: Hiển thị Phiếu khám bệnh với thông tin đã chuẩn hóa và kết quả phân luồng.

# Trường hợp không hợp lệ: Thông báo cảnh báo lỗi cụ thể (validation error).

# Thiết kế thuật toán (Pseudocode)
# Để đảm bảo chương trình không bị lỗi khi người dùng nhập dữ liệu sai, chúng ta thực hiện theo lưu trình: Validation (Kiểm tra dữ liệu) → Decision (Phân luồng) → Output (Xuất kết quả).

# START

# Input ho_ten, tuoi_input

# ho_ten = ho_ten.strip()

# IF ho_ten == "" THEN show "LỖI: Tên trống", STOP

# Convert tuoi_input to integer

# IF tuoi < 0 OR tuoi > 150 THEN show "LỖI: Tuổi phi lý", STOP

# IF tuoi < 6 THEN ket_qua = "Bệnh nhi"
# ELSE IF tuoi >= 80 THEN ket_qua = "Người cao tuổi"
# ELSE ket_qua = "Khám thường"

# Print "Phiếu khám", ho_ten, tuoi, ket_qua

# END

# (2) Triển khai code

def khoi_tao_benh_an():
    print("--- HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN ĐIỆN TỬ ---")
    
    # 1. Nhập liệu
    ho_ten = input("Nhập họ và tên bệnh nhân: ")
    tuoi_input = input("Nhập tuổi: ")

    # 2. Xử lý Bẫy 1: Tên trống hoặc chỉ chứa khoảng trắng
    if not ho_ten.strip():
        print("LỖI: Tên không hợp lệ (không được để trống)!")
        return

    # 3. Xử lý Bẫy 2: Tuổi không phải số hoặc nằm ngoài phạm vi logic (0-150)
    try:
        tuoi = int(tuoi_input)
        if tuoi < 0 or tuoi > 150:
            print("LỖI: Tuổi nằm ngoài phạm vi con người (0-150)!")
            return
    except ValueError:
        print("LỖI: Tuổi phải là một số nguyên hợp lệ!")
        return

    # 4. Phân luồng ưu tiên
    if tuoi < 6:
        phan_loai = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif tuoi >= 80:
        phan_loai = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        phan_loai = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    # 5. Xuất Phiếu khám bệnh
    print("\n" + "="*50)
    print("PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print(f"Họ và tên: {ho_ten.strip()}")
    print(f"Tuổi: {tuoi}")
    print(f"Kết quả: {phan_loai}")
    print("="*50)

# Chạy chương trình
if __name__ == "__main__":
    khoi_tao_benh_an()