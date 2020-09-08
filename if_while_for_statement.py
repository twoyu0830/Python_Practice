k = int(input("구분? 1. 주간, 2. 야간")) #중첩 if문
m = int(input("대상? 1. 대인, 2. 소인"))
if k == 1:
    if m == 1:
        fee = 40000
    else:
        fee = 30000
else:
    if m == 1:
        fee = 30000
    else:
        fee = 20000
print(fee)