wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)
five = 5
one = 1

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print(f"{five}시간에 {wage * five}달러 벌었습니다")  # 여기에 코드를 작성하세요

# "1시간에 5710.8원 벌었습니다." 출력
print(f"{one}시간에 {wage * one * exchange_rate}원 벌었습니다.")  # 여기에 코드를 작성하세요

# "5시간에 28554.0원 벌었습니다." 출력
print(f"{five}시간에 {wage * five * exchange_rate:.1f}원 벌었습니다.")  # 여기에 코드를 작성하세요
