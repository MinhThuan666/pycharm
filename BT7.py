try:
    #Nhập số dòng muốn nhập thỏa mãn <0 t <= 100>
    t = int((input("Nhập số dòng muốn in ra: ")))
    #điều kiện thực hiện đc là phải thỏa mãn đc t>0 và <=100.
    if t < 0:
        print("Nhập số dòng phải lớn hơn 0 !")
    elif t >= 100:
        print("Không quá 100 dòng.")
    # Tạo danh sách rỗng để truyền t vào
    lst_str = []
    for i in range(t):
        str = input(f"Dòng thứ {i+1}: ")
        lst_str.append(str)
    for i in range(len(lst_str)):
        print(f"\nTest {i+1}:")
        lst_word = []
        for j in (lst_str[i].split()):
            # xét j và append nếu thỏa
            if j not in lst_word:
                print(f"{j}", end=" ")
                lst_word.append(j)

except:
    # try except để bắt lỗi khi người dùng nhập sai
    print("Nhập Sai rồi ní ơi ")