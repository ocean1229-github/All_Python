def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    count = 0
    
    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 3:
        return "5000"
    elif count == 4:
        return "50000"
    elif count == 5 and bonus_count == 1:
        return "50000000"
    elif count == 5:
        return "1000000"
    elif count == 6:
        return "1000000000"
    else:
        return "당첨 실패"
    


# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))