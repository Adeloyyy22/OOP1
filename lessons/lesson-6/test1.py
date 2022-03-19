mass = [i for i in range(1_000_000)]

target = 1_000_000

for num in range(len(mass)):
    if target == mass[num]:
        print(num)