packs_of_pens = int(input())
packs_of_markers = int(input())
liters_of_deteregent = float(input())
discount = float(input())
discount_percent = discount * 0.01

price_of_pens = packs_of_pens * 5.8
price_of_markers = packs_of_markers * 7.2
price_of_deteregent = liters_of_deteregent * 1.2

sum_total = price_of_pens + price_of_markers + price_of_deteregent
sum_discount = sum_total - (sum_total * discount_percent)

print(sum_discount)
