deposit_amount = float(input())
deposit_lenght = int(input())
deposit_yearly_interest = float(input())

final_sum = deposit_amount + deposit_lenght * ((deposit_amount * deposit_yearly_interest / 100) / 12)
print(final_sum)
