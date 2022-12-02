try:
    # Nhập số dòng muốn nhập thỏa mãn<0 < t <= 100>
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0:
        print("Nhập số dòng phải lớn hơn 0 !")
    elif t >= 100:
        print("Không quá 100 dòng.")
    lst_str = []
    # cho i chạy từ 0 đến số lượng dòng đã nhập để nhập đúng số chuỗi mong muốn
    for i in range(t):
    # nhập lần lượt các chuỗi cho mỗi dòng
        str = input(f"Dòng thứ {i + 1}: ")
        lst_str.append(str)
    for i in range(len(lst_str)):
        print(f"Test {i + 1}:\n{len(lst_str[i].split())}")
except:
    print("Bạn đã nhập sai!\nVui lòng nhập lại")
    # try except để bắt lỗi khi người dùng nhập sai
