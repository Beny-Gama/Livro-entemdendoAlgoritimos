# Marge Sort é um algoritomo de ordenação: 
# ele algoritimo de busca que usa uma estrategia de Dividir para Donquistar.
# Sua ideia básica consiste em Dividir (o problema em vários subproblemas e resolver esses subproblemas através da recursividade) e Conquistar (após todos os subproblemas terem sido resolvidos ocorre a conquista que é a união das resoluções dos subproblemas).`` 
# é de complexoadade O(n Log n)
# https://www.youtube.com/watch?v=a5LfKZp34d8
# leetcode 148



def findMiddle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def margetwolsit(l1, l2):
    head = listNode()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    return head.next
