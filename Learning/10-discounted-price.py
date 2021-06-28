# 'price' has already been created

# Write your code here

price=-1

if price>=300:
    price=price*0.7
elif price in range(200,300):
    price=price*0.80
elif price in range(100,200):
    price=price*0.90
elif price in range(0,100):
    price=price*0.95


print("price = ",price)