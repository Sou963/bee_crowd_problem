inter = 0
gremio = 0
empates = 0
grenais = 0

while True:

    a, b = map(int, input().split())

    grenais += 1

    if a > b:
        inter += 1

    elif b > a:
        gremio += 1

    else:
        empates += 1

    while True:
        print('Novo grenal (1-sim 2-nao)')
        x = int(input())

        if x == 1 or x == 2:
            break

    if x == 2:
        break

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empates}')

if inter > gremio:
    print('Inter venceu mais')

elif gremio > inter:
    print('Gremio venceu mais')

else:
    print('Nao houve vencedor')