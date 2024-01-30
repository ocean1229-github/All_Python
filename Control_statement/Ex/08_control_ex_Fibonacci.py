# 여기에 코드를 작성하세요
previous = 0
current = 1
i = 1
next_Num = 0

print(i)

while i <= 49:
    next_Num = previous + current
    previous = current
    current = next_Num
    print(next_Num)
    
    i += 1
    
#----------------------------------------------
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1
