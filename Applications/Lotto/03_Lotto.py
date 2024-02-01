def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    count = 0
    i = 0
    while i <= (len(numbers) - 1):
        j = 0
        while j <= (len(winning_numbers) - 1):
            if(numbers[i] == winning_numbers[j]):
                count += 1
            j += 1
        i += 1
    return count
    
    #모범 코드
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))