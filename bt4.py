# 1. Phân tích Input / Output
# Input (Dữ liệu đầu vào)

# Hệ thống nhận 3 biến dạng số nguyên (int):

# Biến	Ý nghĩa	Điều kiện hợp lệ
# age	Tuổi bệnh nhân	< 75
# systolic_bp	Huyết áp tâm thu	90 -> 140
# blood_sugar	Đường huyết	< 150
# Kiểm tra dữ liệu lỗi (Edge Case)

# Nếu bất kỳ giá trị nào:

# Là số âm
# Hoặc nhập sai kiểu dữ liệu

# => In ra:

# Dữ liệu nhập vào không hợp lệ

# và dừng chương trình.

# Output (Kết quả đầu ra)
# Nếu đạt toàn bộ điều kiện:
# ĐỦ ĐIỀU KIỆN PHẪU THUẬT
# Nếu trượt ít nhất 1 điều kiện:
# TỪ CHỐI PHẪU THUẬT
# 2. Đề xuất giải pháp
# Giải pháp 1: Gộp điều kiện (Flat Logic)
# Ý tưởng

# Dùng một câu lệnh if lớn với toán tử logic and.

# Ví dụ:

# if age < 75 and 90 <= systolic_bp <= 140 and blood_sugar < 150:
# Ưu điểm
# Code ngắn
# Dễ viết
# Tốc độ xử lý tốt
# Nhược điểm
# Khó debug khi điều kiện nhiều
# Không biết bệnh nhân trượt tiêu chí nào
# Thông báo thường chung chung
# Giải pháp 2: Điều kiện lồng nhau (Nested If)
# Ý tưởng

# Kiểm tra từng điều kiện theo thứ tự.

# Ví dụ:

# if age < 75:
#     if 90 <= systolic_bp <= 140:
#         if blood_sugar < 150:
# Ưu điểm
# Dễ xác định lỗi cụ thể
# Có thể thông báo chi tiết từng tiêu chí y khoa
# Phù hợp hệ thống bệnh viện thật
# Nhược điểm
# Code dài hơn
# Thụt lề nhiều
# Nếu viết kém sẽ hơi rối. Python mà thụt sai một dấu cách là chương trình đi du lịch sang chiều không gian khác.
# 3. Bảng so sánh hai giải pháp
# Tiêu chí	Flat Logic	Nested If
# Độ ngắn gọn	Cao	Trung bình
# Dễ viết nhanh	Cao	Trung bình
# Dễ đọc khi nhiều điều kiện	Trung bình	Cao
# Thụt lề	Ít	Nhiều
# Debug lỗi	Khó hơn	Dễ hơn
# Thông báo chi tiết	Kém	Tốt
# Giá trị thực tế trong y khoa	Trung bình	Cao
# Khả năng mở rộng	Trung bình	Tốt

# 4. Chốt lựa chọn
# Chọn: Nested If
# Lý do

# Trong môi trường y khoa:

# Tính rõ ràng quan trọng hơn việc code ngắn
# Điều dưỡng cần biết bệnh nhân bị loại vì lý do gì
# Dễ bảo trì và mở rộng thêm tiêu chí sau này

# Ví dụ sau này thêm:

# Nhịp tim
# SpO2
# BMI
# Dị ứng thuốc

# thì cấu trúc kiểm tra tuần tự sẽ dễ quản lý hơn.

# Trade-off
# Code dài hơn một chút
# Nhưng đổi lại:
# dễ đọc,
# dễ debug,
# đúng nghiệp vụ bệnh viện hơn.

try:
    # =========================
    # NHẬP DỮ LIỆU
    # =========================
    age = int(input("Nhập tuổi bệnh nhân: "))
    systolic_bp = int(input("Nhập huyết áp tâm thu: "))
    blood_sugar = int(input("Nhập đường huyết: "))

    # =========================
    # KIỂM TRA DỮ LIỆU ÂM
    # =========================
    if age < 0 or systolic_bp < 0 or blood_sugar < 0:
        print("Dữ liệu nhập vào không hợp lệ")

    else:
        # =========================
        # SÀNG LỌC TIỀN PHẪU
        # =========================

        if age < 75:

            if 90 <= systolic_bp <= 140:

                if blood_sugar < 150:
                    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

                else:
                    print("TỪ CHỐI PHẪU THUẬT")
                    print("Lý do: Đường huyết quá cao")

            else:
                print("TỪ CHỐI PHẪU THUẬT")
                print("Lý do: Huyết áp ngoài ngưỡng an toàn")

        else:
            print("TỪ CHỐI PHẪU THUẬT")
            print("Lý do: Tuổi bệnh nhân vượt giới hạn cho phép")

except ValueError:
    print("Dữ liệu nhập vào không hợp lệ")