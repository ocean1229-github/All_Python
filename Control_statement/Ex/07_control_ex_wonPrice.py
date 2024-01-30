# 여기에 코드를 작성하세요
money = 50000000
dong_money = money
eun_money = 1100000000
year = 1988
standard_year = 2016


# 동일 아저씨 의견
while year < standard_year:
    dong_money += dong_money * 0.12
    year += 1

dong_money = int(dong_money)

if dong_money > eun_money:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format((dong_money - eun_money)))
elif eun_money > dong_money:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(eun_money - dong_money))
else:
    print("가격이 동일합니다!")
