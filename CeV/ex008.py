n = int(input('Uma distancia em metros: '))

km = n / 1000
hm = n / 100
am = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print(f'A media de {n}.0m corresponte a: \n{km}km \n{hm}hm \n{am}am \n{dm}dm \n{cm}cm \n{mm}mm')