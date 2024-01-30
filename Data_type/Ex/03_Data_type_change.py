def calculate_change(payment, cost):
    # 여기에 코드를 작성하세요
    change = payment - cost
    fifty_thousand = change // 50000
    ten_thousand = change%50000 // 10000
    five_thousand = change%50000%10000 // 5000
    thousand = change%50000%10000%5000 // 1000
    print("50000원 지폐: {}장".format(fifty_thousand))
    print("10000원 지폐: {}장".format(ten_thousand))
    print("5000원 지폐: {}장".format(five_thousand))
    print("1000원 지폐: {}장".format(thousand))


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)