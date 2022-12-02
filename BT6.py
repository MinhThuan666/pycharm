try:
    #Nhập số dòng muốn nhập thỏa mãn <0 t <= 100>
    t = int(input("Nhập số bộ test: "))
    #điều kiện thực hiện đc là phải thỏa mãn đc t>0 và <=100.
    if(t > 0 and t <= 100):
        # Cho i chạy từ 0 đến số lượng bộ test đã nhập lúc đầu để nhập đúng số chuỗi mong muốn
        for i in range(t):
            # Nhập lần lượt các chuỗi cho mỗi bộ test
            Str = input(f"Chuỗi string thứ {i + 1}: ")
            Old = input(f"Chuỗi old thứ {i+1}: ")
            New = input(f"Chuỗi new thứ {i+1}: ")
            print(f"Test {i+1}: {Str.replace(Old, New)}")
    else:
        # Thông báo nhập lại cho đúng yêu cầu
        print("Vui lòng nhập lại ")
# Hiển thị ra thông báo khi nhập sai
except:
    print("Bạn đã nhập sai!\nVui lòng nhập lại ")