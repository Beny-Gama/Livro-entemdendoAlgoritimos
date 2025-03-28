num = 1
while num > 0:
    print('-'*20)

    num = int(input('whats the value do you whats for multiplication table: '))

    print('-'*20)
    
    for n in range(1, 10 + 1):
        mult = n * num
        print(f'{num} X {n} = {mult}')
  

