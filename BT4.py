#Bài 4. Liệt kê các từ theo thứ tự xuất hiện trong câu. Các từ phân tách nhau bằng 1 dấu cách
try:
    #Nhập số dòng muốn nhập thỏa mãn<0 < t <= 100>
    t = int(input("Nhập số dòng muốn nhập: "))
    #điều kiện thực hiện đc là phải thỏa mãn đc t>0 và <=100.
    if(t > 0 and t <= 100):
        # Tạo danh sách rỗng để truyền t vào
        list_str = []
        for i in range(t):
            # nhập lần lượt các chuỗi cho mỗi dòng
            Str = input(f"Dòng thứ {i + 1}: ")
            # thêm chuỗi vào danh sách
            list_str.append(Str)
        # cho i chạy từ 0 đến độ dài của danh sách chuỗi
        for i in range(len(list_str)):
            # tạo biến chứa chuỗi là kết quả đầu ra
            output =""
            # list_str[i] dùng i để tham chiếu tới chuỗi trong danh sách
            # sử dụng hàm split() để tách list_str[i] thành các chuỗi con được phân tách bởi khoảng trắng
            # tạo biến String là danh sách chứa các chuỗi con
            String = list_str[i].split()
            # cho x chạy từ 0 đến độ dài danh sách String
            for x in range(len(String)):
                # String[x] truy tham chiếu tới chuỗi con trong danh sách String
                # thêm chuỗi con và khoảng trắng vào chuỗi đầu ra
                output += String[x] + " "
            # in ra dòng 1 dạng Test i (trong đó i là thứ tự bộ test tính từ 1)
            # dòng 2 hiển thị các từ theo thứ tự xuất hiện
            # sử dụng hàm rstrip() để xóa khoảng trắng cuối chuỗi
            print(f"Test {i + 1}:\n{output.rstrip()}")
    else:
        # thông báo nhập lại số dòng cho đúng yêu cầu
        print("Vui lòng nhập lại ")
# hiển thị ra thông báo khi người dùng nhập sai đầu vào
except:
    print("Bạn đã nhập sai!\nVui lòng nhập lại ")
# try except để bắt lỗi khi người dùng nhập sai
