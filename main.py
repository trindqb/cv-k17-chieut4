import cv2 as cv
import numpy as np
import math
import datetime

def draw_clock():
    # Cấu hình khung hình
    width, height = 600, 600
    center = (width // 2, height // 2)
    radius = 250

    print("Đang chạy đồng hồ... Nhấn phím 'Esc' để thoát.")

    while True:
        # Tạo nền màu tím (BGR: 128, 0, 128)
        img = np.full((height, width, 3), (128, 0, 128), dtype=np.uint8)

        # 1. Vẽ mặt đồng hồ và tâm
        cv.circle(img, center, radius, (255, 255, 255), 3)
        cv.circle(img, center, 8, (255, 255, 255), -1)

        # 2. Level 5: Vẽ 60 vạch chỉ phút
        for i in range(60):
            angle = i * 6
            # Tính tọa độ điểm bắt đầu và kết thúc của vạch
            x1 = int(center[0] + (radius - 10) * math.cos(math.radians(angle)))
            y1 = int(center[1] + (radius - 10) * math.sin(math.radians(angle)))
            x2 = int(center[0] + radius * math.cos(math.radians(angle)))
            y2 = int(center[1] + radius * math.sin(math.radians(angle)))
            
            thickness = 3 if i % 5 == 0 else 1
            cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), thickness)

        # 3. Vẽ các số La Mã
        font = cv.FONT_HERSHEY_TRIPLEX
        cv.putText(img, 'XII', (center[0]-35, center[1]-200), font, 1.2, (200, 150, 255), 2)
        cv.putText(img, 'VI', (center[0]-25, center[1]+230), font, 1.2, (200, 255, 150), 2)
        cv.putText(img, 'III', (center[0]+200, center[1]+15), font, 1.2, (255, 150, 150), 2)
        cv.putText(img, 'IX', (center[0]-270, center[1]+15), font, 1.2, (255, 150, 150), 2)

        # 4. Lấy thời gian thực từ hệ thống
        now = datetime.datetime.now()
        h = now.hour % 12
        m = now.minute
        s = now.second

        # 5. Tính toán góc quay (Trừ 90 độ vì 0 độ trong toán học bắt đầu từ hướng 3h)
        # Kim giây: 6 độ mỗi giây
        angle_s = (s * 6) - 90
        # Kim phút: 6 độ mỗi phút + bù thêm theo giây
        angle_m = (m * 6 + s * 0.1) - 90
        # Kim giờ: 30 độ mỗi giờ + bù thêm theo phút
        angle_h = (h * 30 + m * 0.5) - 90

        # 6. Vẽ các kim với màu sắc theo yêu cầu
        # Kim giờ: Xanh dương
        cv.line(img, center, (int(center[0] + 130 * math.cos(math.radians(angle_h))), 
                             int(center[1] + 130 * math.sin(math.radians(angle_h)))), (255, 0, 0), 7)
        # Kim phút: Xanh lá
        cv.line(img, center, (int(center[0] + 180 * math.cos(math.radians(angle_m))), 
                             int(center[1] + 180 * math.sin(math.radians(angle_m)))), (0, 255, 0), 4)
        # Kim giây: Đỏ
        cv.line(img, center, (int(center[0] + 210 * math.cos(math.radians(angle_s))), 
                             int(center[1] + 210 * math.sin(math.radians(angle_s)))), (0, 0, 255), 2)

        # Hiển thị kết quả
        cv.imshow('Clock Level 5', img)

        # Đợi 1 giây (1000ms) rồi lặp lại, nếu nhấn Esc thì thoát
        if cv.waitKey(1000) == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    draw_clock()