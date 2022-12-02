#Bài 1. Viết hoa toàn bộ chữ cái đầu từ trong câu cho trước nhập vào từ bàn phím. Các chữ cái còn lại viết thường.

try:
    #Nhập số dòng muốn nhập thỏa mãn <0 t <= 100>
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0:
    #điều kiện thực hiện đc là phải thỏa mãn đc t>0 và <=100.
        print("Nhập số dòng phải lớn hơn 0 ")
    elif t >= 100:
        print("Không quá 100 dòng.")
    # Tạo danh sách rỗng để truyền t vào
    lst_str = []
    # Chạy i để truyền t vào lst_str
    for i in range(t):
        str = input(f"Dòng thứ {i+1}: ")
        lst_str.append(str)
    # Xuất ra lần lượt theo độ dài lst
    for i in range(len(lst_str)):
        print(f"Test {i+1}: \n {lst_str[i].title()}")
except:
    print("Nhập không hợp lệ! ")
#try except để bắt lỗi khi người dùng nhập sai
