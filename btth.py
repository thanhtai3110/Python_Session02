import datetime

# 1. Nhập thông tin
name = input("Nhập tên bệnh nhân: ").strip()
birth_year = int(input("Nhập năm sinh: "))
days_sick = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
base_cost = float(input("Nhập chi phí khám: "))

current_year = datetime.date.today().year

# 2. Kiểm tra dữ liệu hợp lệ
is_valid = True
if not name:
    print("Lỗi: Tên không được để trống!")
    is_valid = False
elif not (1900 <= birth_year <= current_year):
    print("Lỗi: Năm sinh không hợp lệ!")
    is_valid = False
elif days_sick < 0:
    print("Lỗi: Số ngày bệnh phải >= 0!")
    is_valid = False
elif not (30 <= temperature <= 45):
    print("Lỗi: Nhiệt độ phải trong khoảng 30 - 45°C!")
    is_valid = False
elif base_cost <= 0:
    print("Lỗi: Chi phí khám phải > 0!")
    is_valid = False

if is_valid:
    # 3. Tính toán thông tin
    age = current_year - birth_year
    total_cost = base_cost + (base_cost * 0.1) # Phụ phí 10%
    
    # 4. Phân loại tình trạng sức khỏe
    if temperature > 38 and days_sick > 3:
        status = "Nguy hiểm"
    elif temperature > 38:
        status = "Sốt cao"
    elif temperature > 37.5:
        status = "Sốt nhẹ"
    else:
        status = "Bình thường"
        
    # 5. Đánh giá mức độ ưu tiên (Nested If)
    priority = ""
    if status == "Nguy hiểm":
        if age > 60:
            priority = "Cấp cứu"
        else:
            priority = "Ưu tiên cao"
    else:
        priority = "Bình thường"
        
    # 6. Đánh giá mức chi phí (Toán tử ba ngôi)
    cost_level = "Cao" if total_cost > 500000 else "Thấp"
    
    # 7. Hiển thị kết quả
    print("\n--- KẾT QUẢ ĐÁNH GIÁ ---")
    print(f"Bệnh nhân: {name} ({age} tuổi)")
    print(f"Tình trạng: {status}")
    print(f"Ưu tiên: {priority}")
    print(f"Tổng chi phí: {total_cost:,.0f} VNĐ ({cost_level})")