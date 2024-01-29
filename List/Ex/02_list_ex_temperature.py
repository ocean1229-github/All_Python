# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 여기에 코드를 작성하세요
    celsius = (fahrenheit - 32) * 5 / 9
    celsius = round(celsius, 1)
    return celsius

temperature_list = [40, 15, 32, 64, -4, 11]
celsius_list = []

i = 0
while i < len(temperature_list):
    celsius_list.append(fahrenheit_to_celsius(temperature_list[i]))
    i += 1


print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요
print("섭씨 온도 리스트: {}".format(celsius_list))  # 섭씨 온도 출력
