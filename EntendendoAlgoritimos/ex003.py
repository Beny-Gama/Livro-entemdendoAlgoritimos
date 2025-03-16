# def procure_pela_chave(caixa_pricipal):
#     pilha = main_box.crie_uma_pilha_para_busca()
#     while pilha is not vazia:
#         caixa = pilha.pegue.caixa()
#         for item in caixa:
#             if item.e_uma_caixa():
#                 pilha.append(item)
#             elif item.e_uma_chave():
#                 print('achei a chabe')


# recursividade
def contagemRegresiva(num):
    print(num)
    if num < 1:
        return
    else:
        contagemRegresiva(num - 1)

contagemRegresiva(10)