# 1. Phân tích lỗi (Root Cause Analysis)
# Luồng thực thi "từ trên xuống dưới"
# Trong cấu trúc if-elif-else, chương trình sẽ kiểm tra các điều kiện theo thứ tự từ trên xuống dưới. Ngay khi tìm thấy một điều kiện đầu tiên đúng (True), chương trình sẽ thực thi khối lệnh tương ứng và bỏ qua toàn bộ các khối elif và else còn lại trong cấu trúc đó.

# Dò luồng với trường hợp heart_rate = 135
# Chương trình kiểm tra điều kiện đầu tiên: if heart_rate > 100:

# Với 135, biểu thức 135 > 100 là True.

# Chương trình in ra: "Priority: YELLOW - Abnormal. Monitor closely."

# Vì điều kiện này đã thỏa mãn, chương trình kết thúc cấu trúc kiểm tra và nhảy thẳng đến lệnh cuối cùng (print("Triage process completed.")).

# Khối elif heart_rate > 120: hoàn toàn không bao giờ được kiểm tra vì điều kiện > 100 đã "chặn" luồng đi ngay từ đầu.

# Nguyên nhân: Lỗi nằm ở việc sắp xếp các khoảng điều kiện. Điều kiện bao quát hơn (> 100) đã được đặt lên trước điều kiện cụ thể hơn (> 120), khiến các trường hợp nguy kịch bị "nhầm lẫn" thành trạng thái bất thường.

# 2. Sửa lỗi (Refactored Code)

print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Sắp xếp lại thứ tự ưu tiên từ nghiêm trọng nhất đến ổn định
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    # Nếu không thỏa mãn các điều kiện trên, nhịp tim nằm trong khoảng [60, 100]
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")