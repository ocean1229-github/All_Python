# 여기에 코드를 작성하세요
i = 1
count = 0

while i < 1000:
    if(i % 2 == 0 or i % 3 == 0):
        count += i
    i += 1
    
print(count)