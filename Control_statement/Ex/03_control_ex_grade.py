def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 여기에 코드를 작성하세요
    if(total >= 90):
        print("A")
    elif(total >= 80):
        print("B")
    elif(total >= 70):
        print("C")
    elif(total >= 60):
        print("D")
    else:
        print("F")


# 테스트 코드
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)