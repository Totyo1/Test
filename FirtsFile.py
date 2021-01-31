budget = float(input())
statists = int(input())
clothes_per_statist = float(input())

dekore = budget * 0.1
if statists > 150:
    clothes_per_statist = clothes_per_statist * 0.9
money = statists*clothes_per_statist + dekore

if money > budget:
    print("Not enough money!")
    print(f"Wingard needs {money - budget} leva more.")
else:
    print('Action!')
    print(f'Wingard starts filming with {"%.2f" % float(budget-money)} leva left.')
    print('da eba mama mu')