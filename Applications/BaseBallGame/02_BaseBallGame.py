def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 여기에 코드를 작성하세요
    while len(new_guess) < 3:
        number = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        
        if number < 0 and number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")

        elif number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            
        else:
            new_guess.append(number)
    
    return new_guess
    
    
# 테스트 코드
print(take_guess())