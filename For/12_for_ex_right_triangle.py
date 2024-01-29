for i in range(1, 201):
    for j in range(1, 202):
        for k in range(1, 400):
            if( i ** 2 + j ** 2 == k ** 2 and i + j + k == 400 and i < j < k):
                print(i * j * k)