def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 여기에 코드를 작성하세요
    i = 0
    while i < 3:
        if(guesses[i] == solution[i]):
        elif (guesses[i] == solution[i + 1]):
            strike_count += 1
            ball_count += 1
        elif (guesses[i] == solution[i + 2]):
            ball_count += 1
        i += 1
            
    return strike_count, ball_count


# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
