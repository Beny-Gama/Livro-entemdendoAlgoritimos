tabelaDoBrasileirão = ('Botafogo','Palmeiras','flamengo', 'fortaleza','Internarical', 'São Paulo', 'Corintians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitoria', 'Atlétuco/MG', 'Fluminece', 'Grêmio', 'Juventos', 'RB Bragantino', 'Atletico/PR', 'Criciúma', 'Atlético/GO', 'Cuiabá')

print(f'=-'*30, '\n')
print(f'Lista de times: {tabelaDoBrasileirão}')

print(f'=-'*30, '\n')
print(f'5 primeros Colocados: {tabelaDoBrasileirão[:5]}')

print(f'=-'*30, '\n')
print(f'4 ultimos Colocados: {tabelaDoBrasileirão[-4:]}')

print(f'=-'*30, '\n')
print(f'Ordem alfabetica: {sorted(tabelaDoBrasileirão)}')

print(f'=-'*30, '\n')
print(f'O Vasco está na posição: {tabelaDoBrasileirão.index("Vasco") + 1} do Brasileirão')