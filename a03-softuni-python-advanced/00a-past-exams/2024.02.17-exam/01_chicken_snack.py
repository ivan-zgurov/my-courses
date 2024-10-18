money = list(map(int, input().split()))
prices = list(map(int, input().split()))

food_count = 0

while money and prices:
    current_money = money.pop()  # Take last amount of money
    current_price = prices.pop(0)  # Take first price

    if current_money == current_price:
        food_count += 1
    elif current_money > current_price:
        food_count += 1
        change = current_money - current_price
        if money:
            money[-1] += change

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count > 1:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
