numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def password (numbers):
    passwo = ''
    for i in range(1, numbers):
        for j in range(i + 1, numbers):
            if numbers % (i + j) == 0:
                passwo += str(i) + str(j)
    return passwo

print(password(int(input('Введите пароль от 3 до 20:'))))

