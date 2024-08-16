yearly_training_fee = int(input())

price_of_shoes = 0.6 * yearly_training_fee
price_of_kit = 0.8 * price_of_shoes
price_of_ball = 0.25 * price_of_kit
price_of_accessories = 0.2 * price_of_ball

total_expences = yearly_training_fee + price_of_shoes + price_of_kit + price_of_ball + price_of_accessories
print(total_expences)
