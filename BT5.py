try:
    #Nhập số dòng muốn nhập thỏa mãn<0 t <= 100>
    t = int(input("Nhập số dòng muốn nhập: "))
    #điều kiện thực hiện đc là phải thỏa mãn đc t>0 và <=100.
    if(t > 0 and t <= 100):
        for i in range(t):
            # nhập lần lượt các chuỗi cho mỗi dòng
            Str1 = input(f"Dòng thứ {i + 1}: ")
            # nhập chuỗi con
            Str2 =input(f"Chuỗi con thứ {i+1}: ")
            # sử dụng hàm count() để đếm số lần xuất hiện của chuỗi con
            # in ra kết quả trên 1 dòng dạng Test i: kết quả (Trong đó i là thứ tự bộ test tính từ 1)
            print(f"Test {i+1}: {Str1.count(Str2, 0, len(Str1))}")
    else:
        # thông báo nhập lại số dòng cho đúng yêu cầu
        print("Vui lòng nhập lại số dòng ")
# hiển thị ra thông báo khi người dùng nhập sai đầu vào
except:
 # try except để bắt lỗi khi người dùng nhập sai
    print("Bạn đã nhập sai!\nVui lòng nhập lại ")
