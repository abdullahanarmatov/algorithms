n = int(input())
minuti = n * 45
hours = minuti // 60
minut = minuti % 60

five = (n // 2) * 5
fifteen = (n // 2 + (n % 2 - 1)) * 15
minut = minut + five +fifteen
hours = hours + (minut // 60)
minut = minut % 60

print(hours + 9, minut)

