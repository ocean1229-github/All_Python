from random import randint


def generate_numbers(n):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    bonus_number = generate_numbers(6)
    bonus_number.sort()
    bonus_number.append(randint(1, 45))
    
    return bonus_number

# 테스트 코드
print(draw_winning_numbers())