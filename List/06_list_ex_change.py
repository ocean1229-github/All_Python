# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 여기에 코드를 작성하세요
    usd_price = krw / 1000
    usd_price = round(usd_price, 1)
    
    return usd_price

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 여기에 코드를 작성하세요
    jpy_price = usd * 125
    
    return jpy_price
    


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
# 여기에 코드를 작성하세요
i = 0
usd_prices = []
while i < len(prices):
    usd_prices.append(krw_to_usd(prices[i]))
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(usd_prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
# 여기에 코드를 작성하세요
i = 0
jpy_prices = []
while i < len(prices):
    jpy_prices.append(usd_to_jpy(usd_prices[i]))
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(jpy_prices))