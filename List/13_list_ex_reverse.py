numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 여기에 코드를 작성하세요
reverse_numbers = []

for i in range(len(numbers)):
    reverse_numbers.insert(0, numbers[i]) 
    
numbers = reverse_numbers

print("뒤집어진 리스트: " + str(numbers))

