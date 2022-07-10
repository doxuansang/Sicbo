import random

# Game tài xỉu (đôi khi còn được gọi là SicBo hay over – under) là một trò chơi của Trung Quốc có từ thời cổ đại.
# quy tắc của trò chơi này tương đối phức tạp và có nhiều mức thưởng khác nhau.
# Tuy nhiên, ở trong phạm vi của bài này, chúng ta chỉ cần hiểu cách chơi đơn giản nhất: chọn tài hay xỉu
# Nếu ba viên xúc xắc trả về tổng số nút từ 4 đến 10 thì xỉu thắng
# Ngược lại, nếu tổng số nút trả về từ 11 đến 17 thì tài thắng
# Lưu ý, khi ba viên xúc xắc trả về cùng một số, tài hay xỉu đều thua
# Tỉ lệ cho đặt cược này là 1:1

# Tạo 1 giải thuật giúp A có thể luôn có lãi khi tham gia trò chơi này
# không có giải thuật nào như thế cả,
# vì rõ ràng đây là trò chơi may rủi, xác suất thắng cũng không tương xứng với lợi nhuận (nhỏ hơn)
# khả năng thắng là 105/216 (<50%) trong khi tỷ lệ cược chỉ là 1:1
# tuy nhiên, có giải thuật giúp khả năng có lãi của A cao hơn đáng kể
# tỷ lệ có lãi của thuật toán này có thể đạt đến gần 100%

finance = 1024  # số tiền bắt đầu 2^10
# số tiền đặt cược lần đầu tiên bằng 1
# mặc định đánh cược vào tài (từ 11 đến 17 nút)
# nguyên tắc ở đây là:
# số tiền đặt cược lần sau phải lớn hơn tổng số tiền những lần trước
# sao cho khi thắng, tổng số tiền nhận được phải nhiều hơn tiền vốn ban đầu (có lãi)
# thật ra chỉ cần đơn giản gấp đôi là được, thua ở đâu gấp đôi ở đó
# ngay khi thắng liền dừng

def bet(i, finance):
    while finance > i:  # số tiền vốn còn lại phải nhiều hơn số tiền định đặt cược
        finance = finance - i  # số tiền vốn còn lại sau khi đặt cược
        a = random.randint(1, 6)  # a là giá trị số nút của xúc xắc thứ nhất
        b = random.randint(1, 6)  # b là giá trị số nút của xúc xắc thứ hai
        c = random.randint(1, 6)  # c là giá trị số nút của xúc xắc thứ ba
        tx = a+b+c  # tx là tổng giá trị của ba xúc xắc
        # giá trị dự đoán từ 11 đến 17, nhưng trừ TH a=b=c
        if a == b and b == c and a == c:
            return bet(i*2, finance)
        elif tx >= 11 and tx <= 17:
            return 1
        else:
            return bet(i*2, finance)
    return 0

# thử nghiệm với 1 tỷ lần thử (nói xạo á, 1 triệu lần thôi)
tl = 0
for i in range(1000000):
    if bet(1, finance) == 1:
        tl = tl + 1
tl = tl/10000

print("Xác suất có lãi là: {}%".format(tl))

# xác suất chính xác là bao nhiêu ?
# ba viên xúc xắc có giá trị số nút từ 1 đến 6
# dễ nhận thấy có 6.6.6 = 216 trường hợp có thể xảy ra
# trong đó có 6 trường hợp số nút 3 viên giống nhau
# còn lại một nửa trường hợp là tài, một nửa là xỉu
# suy ra, khả năng thắng của tài hay xỉu đều bằng 105/216
# và khả năng thua là 111/216 (vấn đề này mình đã nói ngay từ đầu)
# xác suất tính bằng công thức: 1 - (111/216)^k
# trong đó k là hệ số trong số tiền đặt cược: 2^k

# làm sao để đạt đến tỷ lệ chiến thắng 100%
# đó là khi số tiền vốn ban đầu đạt đến vô hạn (không thể xảy ra trong thực tế)
# tiền vốn càng lớn, tỷ lệ thắng càng cao
# bởi vì số lần có thể sai càng nhiều






