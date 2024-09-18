numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def password (number):
    passwo = []
    for i in range(1, number):
        for j in range(i + 1, number + 1):
            if number % (i + j) == 0:
                passwo = i + j
                return passwo



print(password(int(input('Введите пароль от 3 до 20:'))))












