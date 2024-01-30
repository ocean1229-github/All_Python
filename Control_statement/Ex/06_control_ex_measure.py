# 여기에 코드를 작성하세요
i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print("120의 약수는 총 {}개 입니다.".format(count))