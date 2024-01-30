total = 0
# 자리수 합 리턴
def sum_digit(num):
    # 여기에 코드를 작성하세요
    global total
    sum_num = 0
    for j in range(len(num)):
        sum_num += int(num[j])
        j += 1
    total += sum_num

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 여기에 코드를 작성하세요
for i in range(1, 1001):
    now_num = str(i)
    sum_digit(now_num)
    i += 1
print(total)