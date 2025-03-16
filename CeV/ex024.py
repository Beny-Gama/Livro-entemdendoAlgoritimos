cidade = str(input('Em que cidade vc nasceu? ')).strip()
santo = False
if 'santo' in cidade.lower(): santo = True
print(f'A cidade {cidade} contem {santo}')
