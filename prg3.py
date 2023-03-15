A = int(input())
C = int(input())
# amount_A = A * 37550.0
# amount_c = C*(37550.0//3)
# total = amount_A + amount_c
# total=(total*0.07)+total
# discount = (total*0.10)
# final_amount=total - discount
# print(final_amount)

final = ((((A*37550)+(C*(37550.0/3)))*0.07)*0.90)
print (final)