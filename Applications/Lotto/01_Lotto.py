from random import randint

def generate_numbers(n):
    # 여기에 코드를 작성하세요
    my_number = []
    i = 0
    while i <= 5:
        number = randint(1, 45)
        my_number.append(number)
        i += 1
    return my_number


# 테스트 코드
print(generate_numbers(6))

# 모범답안 -> 위의 코드는 똑같은 수가 겹칠 수 도 있다.
from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


# 테스트 코드
print(generate_numbers(6))
