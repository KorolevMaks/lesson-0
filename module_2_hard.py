def password(n) :
    n = n + 1
    for i in range(n) :
        password_ = ''
        for j in range(1,21) :
            for h in range(1,21) :
                if j + h == i and j < h  or i % (j + h) == 0 and j < h :
                    password_ = password_ + f'{j}{h}'
    return password_
print(password(8))
