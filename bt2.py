# 1. Phân tích lỗi (Root Cause Analysis)
# Toán tử bị sử dụng sai
# Trong dòng code if donor_age >= 18 or donor_weight >= 50:, hệ thống đang sử dụng toán tử or (hoặc).

# Toán tử or: Chỉ cần một trong hai điều kiện đúng, kết quả toàn bộ biểu thức sẽ là True.

# Toán tử and: Cần cả hai điều kiện cùng đúng, kết quả mới là True.

# Dò luồng với Test Case: donor_age = 16, donor_weight = 55
# Chương trình kiểm tra: (16 >= 18) or (55 >= 50)

# 16 >= 18 là False.

# 55 >= 50 là True.

# Biểu thức False or True trả về kết quả là True.

# Kết quả: Hệ thống in "ĐỦ ĐIỀU KIỆN" mặc dù người này chưa đủ 18 tuổi. Đây chính là lỗ hổng nghiêm trọng.

# 2. Sửa lỗi (Refactored Code)

print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Kiểm tra đồng thời cả 2 điều kiện bằng toán tử 'and'
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    
    # Giải thích thêm lý do cho người dùng (tùy chọn nhưng cần thiết)
    if donor_age < 18:
        print("- Reason: Minimum age requirement is 18.")
    if donor_weight < 50:
        print("- Reason: Minimum weight requirement is 50kg.")

print("Triage process completed.")