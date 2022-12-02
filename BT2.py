try:
    #Nhập số dòng muốn nhập thỏa mãn<0 < t <= 100>
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0:
        # điều kiện thực hiện đc là phải thỏa mãn đc t>0 và <=100.
        print("Nhập Lại")
    elif t >= 100:
        print("Không quá 100 dòng.")
    lst_str = []
    for i in range(t):
        word = input(f"Dòng thứ {i+1}: ")
        lst_str.append(word)
    for i in range(len(lst_str)):
        ng_am = 0
        ph_am = 0
        # lst_str chữ thường để khi chạy vòng lặp ko cần pb hoa thường
        lst_str[i].lower()
        for x in (lst_str[i]):
            # Kiểm tra điều kiện x có phải là nguyên âm hay kh
            if (x == "a" or x == "i" or x == "o" or x == "u" or x == "e"):
                ng_am += 1
                #nếu thỏa thì ng_am+1
            elif x == " ":
                #nếu x là khoản trống thì bỏ qua
                continue
            else:
                # nếu thỏa thì ph_am+1
                ph_am += 1
        print(f"Test {i+1}: \n Số nguyên âm trong chuỗi là: {ng_am} \n Số phụ âm trong chuỗi là: {ph_am} ")
except:
    print("Nhập không hợp lệ! ")
#try except để bắt lỗi khi người dùng nhập sai
