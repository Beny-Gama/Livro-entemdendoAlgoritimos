# 605. Can Place Flowers

def canPlaceFlowers(flowerbed, n):
        final = len(flowerbed)
        cont = 0
        
        for i in range(final):
            if flowerbed[i] == 0:
                esquerda = flowerbed[i - 1] if i > 0 else 0
                direita  = flowerbed[i + 1] if i < final - 1 else 0
                if esquerda == 0 and direita == 0:
                    flowerbed[i] = 1
                    cont += 1
                    if cont >= n:
                        return True
        return cont >= n



def canPlaceFlowers2(flowerbed, n):
        cont = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                esquerda = (flowerbed[i - 1] if i < 0 else 1)
                direita = (flowerbed[i + 1])
                
                if direita > len(flowerbed):
                    break
                
                if esquerda == 0 or direita == 0:
                    flowerbed[i] = 1
                    cont += 1

        return True if cont >= n else False


def canPlaceFlowers1(flowerbed, n):
    cont = 0
    for i in range(len(flowerbed)):
        if flowerbed[i - 1] != 1 or flowerbed[i + 1] != 1:
             cont += 1

    if cont >= n:
        return True
    else:
        return False



flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))


flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))


flowerbed = [1,0,0,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))