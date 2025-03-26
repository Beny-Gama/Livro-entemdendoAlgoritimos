# 1768. Merge Strings Alternately

def margeString1(word1, word2):      
    fra = ''
    for l1, l2 in zip(word1, word2):
        fra += l1 + l2
    return fra

# entendedo zep
def margeString2(*iteravais):
    iteradores = [iter(it) for it in iteravais]
    while True:
        try:
            yield tuple(next(it) for it in iteradores)
        except StopIteration:
            break
    

word1, word2 = "abce", "pq"
print('1: ', margeString1(word1, word2))
print('2: ', margeString2(word1, word2))